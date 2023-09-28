# -*- coding: utf-8 -*-
from odoo import api, fields, models


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    weather_api_keys = fields.Boolean(string="Weather API Key")
    api_keys = fields.Char(string="API Key", help="Api keys for weather "
                                                  "calculation")
    location = fields.Char(string="Location", help="Current location to "
                                                   "calculate the weather")

    @api.model
    def set_values(self):
        """Set values for fields creating in settings"""
        res = super(ResConfigSettings, self).set_values()
        self.env['ir.config_parameter'].sudo().set_param(
            'weather_api_keys', self.weather_api_keys)
        self.env['ir.config_parameter'].sudo().set_param(
            'api_keys', self.api_keys)
        self.env['ir.config_parameter'].sudo().set_param(
            'location', self.location)
        return res

    @api.model
    def get_values(self):
        """Get values for fields creating in settings"""
        res = super(ResConfigSettings, self).get_values()
        ICPSudo = self.env['ir.config_parameter'].sudo()
        res.update(
            weather_api_keys=ICPSudo.get_param('weather_api_keys'),
            api_keys=ICPSudo.get_param('api_keys'),
            location=ICPSudo.get_param('location'),
        )
        return res
