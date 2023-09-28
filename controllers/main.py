# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request
import requests
from datetime import date


class WeatherController(http.Controller):
    """Define a route to fetch weather data"""

    @http.route('/fetch_weather_settings', type='json', auth='user')
    def fetch_weather_settings(self):
        """Retrieve weather settings values from the backend"""
        settings = request.env['res.config.settings'].sudo().get_values()
        return {
            'weather_api_keys': settings['weather_api_keys'],

        }

    @http.route('/fetch_weather_data', type='json', auth='user')
    def fetch_weather_data(self):
        """Retrieve weather settings values from the backend"""
        settings = request.env['res.config.settings'].sudo().get_values()
        if settings['weather_api_keys'] and settings['location']:
            api_key = settings['api_keys']
            location = settings['location']
            api_url = (f"https://api.openweathermap.org/data/2.5/weather?q="
                       f"{location}&appid={api_key}")

            try:
                response = requests.get(api_url)
                data = response.json()
                if 'main' in data and 'temp' in data['main']:
                    weather_icon = data['weather'][0]['icon']
                    icon_url = f"http://openweathermap.org/img/wn/{weather_icon}.png"

                    return {
                        'date': date.today(),
                        'temperature': data['main']['temp'],
                        'humidity': data['main']['humidity'],
                        'description': data['weather'][0]['description'],
                        'icon': icon_url,
                        'place': data['name'],
                    }
            except Exception as e:
                print("Error fetching weather data:", e)

        return False
