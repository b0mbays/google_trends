DOMAIN = "google_trends"

def setup(hass, config):
    hass.helpers.discovery.load_platform("sensor", DOMAIN, {}, config)
    return True