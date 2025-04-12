from homeassistant import config_entries
import voluptuous as vol
import homeassistant.helpers.config_validation as cv

from .const import DOMAIN

class F1FlowHandler(config_entries.ConfigFlow, domain=DOMAIN):
    VERSION = 1

    async def async_step_user(self, user_input=None):
        errors = {}

        if user_input is not None:
            # Skapa konfigurationsobjektet
            return self.async_create_entry(
                title=user_input["sensor_name"],  # Titeln som visas i HA
                data=user_input                   # Spara hela user_input i entry.data
            )

        # Visa formulär för att ange sensor-namn
        data_schema = vol.Schema({
            vol.Required("sensor_name", default="F1"): cv.string
        })

        return self.async_show_form(
            step_id="user",
            data_schema=data_schema,
            errors=errors
        )