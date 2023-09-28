{
    "name": "Weather notification",
    "version": "16.0.1.0.0",
    "author": "cybrosys",
    'category': 'Sales',
    "description": "Weather notification",
    'license': 'LGPL-3',
    "depends": [
        "base",
        "sale",
        'web',
    ],
    "data": [
        'views/res_config_settings_view.xml',
    ],
    'assets': {
        'web.assets_backend':
            ['weather_notification/static/src/js/systray_icon.js',
             'weather_notification/static/src/xml/weather_notification_view.xml',
             'weather_notification/static/src/css/systray_dropdown.css',
             ],
    },
    'auto-install': True,
    "application": True,
    "installable": True,

}
