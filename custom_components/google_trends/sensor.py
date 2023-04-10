import logging
import voluptuous as vol

from homeassistant.components.sensor import PLATFORM_SCHEMA
from homeassistant.const import CONF_NAME
import homeassistant.helpers.config_validation as cv
from homeassistant.helpers.entity import Entity
from .google_trends import get_top_trends

_LOGGER = logging.getLogger(__name__)

CONF_COUNTRY_CODE = "country_code"
CONF_UPDATE_INTERVAL = "update_interval"

DEFAULT_NAME = "Google Trends"
DEFAULT_COUNTRY_CODE = "united_kingdom"
DEFAULT_UPDATE_INTERVAL = 60


async def async_setup_entry(hass, config_entry, async_add_entities):
    country_code = config_entry.data[CONF_COUNTRY_CODE]
    update_interval = config_entry.data[CONF_UPDATE_INTERVAL]
    trends_count = config_entry.data[CONF_TRENDS_COUNT]

    trends = get_top_trends(country_code, count=trends_count)

    async_add_entities(
        [
            GoogleTrendsSensor(trends, idx, update_interval, country_code)
            for idx in range(len(trends))
        ],
        True,
    )


class GoogleTrendsSensor(Entity):
    def __init__(self, trends, idx, interval, country_code):
        self._trends = trends
        self._idx = idx
        self._interval = interval
        self._country_code = country_code

    @property
    def name(self):
        return f"Google Trend {self._idx + 1}"

    @property
    def state(self):
        return self._trends[self._idx]

    @property
    def should_poll(self):
        return True

    @property
    def icon(self):
        return "mdi:google"

    @property
    def unique_id(self):
        return f"google_trend_{self._idx + 1}"

    def update(self):
        self._trends = get_top_trends(self._country_code, count=3)
