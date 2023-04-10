import logging
import voluptuous as vol

from homeassistant.components.sensor import PLATFORM_SCHEMA
from homeassistant.const import CONF_NAME
from datetime import timedelta
import homeassistant.helpers.config_validation as cv
from homeassistant.helpers.entity import Entity
from .google_trends import get_top_trends
from .const import CONF_COUNTRY_CODE, CONF_UPDATE_INTERVAL, CONF_TRENDS_COUNT

_LOGGER = logging.getLogger(__name__)

CONF_COUNTRY_CODE = "country_code"
CONF_UPDATE_INTERVAL = "update_interval"

DEFAULT_NAME = "Google Trends"
DEFAULT_COUNTRY_CODE = "united_kingdom"
DEFAULT_UPDATE_INTERVAL = 60


async def async_setup_entry(hass, config_entry, async_add_entities):
    """Set up the Google Trends sensors."""
    country_code = config_entry.options.get(CONF_COUNTRY_CODE, DEFAULT_COUNTRY_CODE)
    trends_count = config_entry.options.get(CONF_TRENDS_COUNT, DEFAULT_TRENDS_COUNT)
    update_interval = timedelta(
        minutes=config_entry.options.get(CONF_UPDATE_INTERVAL, DEFAULT_UPDATE_INTERVAL)
    )

    trends = await hass.async_add_executor_job(
        get_top_trends, str(country_code), trends_count
    )

    async_add_entities(
        [GoogleTrendsSensor(trends, update_interval, country_code)], True
    )

class GoogleTrendsSensor(Entity):
    def __init__(self, trends, interval, country_code, idx):
        """Initialize the Google Trends sensor."""
        self._trends = trends
        self._interval = interval
        self._country_code = country_code
        self._idx = idx

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
        self._trends = get_top_trends(self._country_code, count=len(self._trends))