/** @odoo-module **/
import { registry } from "@web/core/registry";
import { useService } from "@web/core/utils/hooks";
import { Component } from "@odoo/owl";
import core from 'web.core';
import { useState } from "@odoo/owl";


class SystrayIcon extends Component {
    setup() {
        super.setup(...arguments);
        this.action = useService("action");
        this.rpc = useService("rpc");
        this.isDropdownOpen = false;
        this.state = useState({ weatherApiKeys: false });
        this.fetchWeatherApiKeys();
        this.fetchWeatherData = async () => {
            try {
                const response = await this.rpc("/fetch_weather_data", {});

                if (response) {
                    this.weatherData = response;
                }
            } catch (error) {
                console.error("Error fetching weather data", error);
            }
        };
    }

    async fetchWeatherApiKeys() {
        try {
            const settings = await this.rpc("/fetch_weather_settings", {});
            if (settings) {
                this.state.weatherApiKeys = settings.weather_api_keys || false;
            }
        } catch (error) {
            console.error("Error fetching weather API keys", error);
        }
    }

    _onClick() {
        this.fetchWeatherData().then(() => {
            this.isDropdownOpen = !this.isDropdownOpen;
            this.render();
        });
    }
}
SystrayIcon.template = "systray_icon";
export const systrayItem = { Component: SystrayIcon };
registry.category("systray").add("SystrayIcon", systrayItem, { sequence: 1 });

