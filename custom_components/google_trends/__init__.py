from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant
from homeassistant.helpers.typing import ConfigType
from homeassistant.helpers import config_entry_oauth2_flow
from homeassistant.helpers.typing import ConfigType
from homeassistant.config_entries import ConfigEntry, OptionsFlowHandler


from .const import DOMAIN

async def async_setup(hass: HomeAssistant, config: ConfigType):
    return True

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry):
    hass.async_create_task(
        hass.config_entries.async_forward_entry_setup(entry, "sensor")
    )
    return True

async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry):
    return await hass.config_entries.async_forward_entry_unload(entry, "sensor")

class GoogleTrendsOptionsFlowHandler(OptionsFlowHandler):
    """Handle Google Trends options."""

    def __init__(self, config_entry: ConfigEntry):
        """Initialize options flow."""
        self.config_entry = config_entry

    async def async_step_init(self, user_input=None):
        """Manage the options."""
        if user_input is not None:
            return self.async_create_entry(title="", data=user_input)

        options = {
            vol.Optional(
                CONF_UPDATE_INTERVAL,
                default=self.config_entry.options.get(
                    CONF_UPDATE_INTERVAL, DEFAULT_UPDATE_INTERVAL
                ),
            ): int,
            vol.Optional(
                CONF_COUNTRY_CODE,
                default=self.config_entry.options.get(
                    CONF_COUNTRY_CODE, DEFAULT_COUNTRY_CODE
                ),
            ): str,
            vol.Optional(
                CONF_TRENDS_COUNT,
                default=self.config_entry.options.get(
                    CONF_TRENDS_COUNT, DEFAULT_TRENDS_COUNT
                ),
            ): int,
        }

        return self.async_show_form(
            step_id="init",
            data_schema=vol.Schema(options),
        )