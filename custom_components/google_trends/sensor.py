import logging
from datetime import timedelta
from homeassistant.helpers.entity import Entity
from . import DOMAIN
from .google_trends import get_top_trends

_LOGGER = logging.getLogger(__name__)

SCAN_INTERVAL = timedelta(minutes=30)

def setup_platform(hass, config, add_entities, discovery_info=None):
    country_code = hass.config.as_dict()["homeassistant"]["external_url"].split(".")[-1]
    add_entities([TwitterTrendsSensor(country_code)], True)

class TwitterTrendsSensor(Entity):
    def __init__(self, country_code):
        self._country_code = country_code
        self._state = None
        self._trends = []

    @property
    def name(self):
        return "Twitter Trends"

    @property
    def state(self):
        return self._state

    @property
    def extra_state_attributes(self):
        return {"trends": self._trends}

    def update(self):
        self._trends = get_top_trends(self._country_code, count=5)
        self._state = len(self._trends)