# -*- coding: utf-8 -*-
{
    'name': "Fleet Management",
    'summary': "Manage your fleet of vehicles, drivers, and maintenance.",
    'description': """
        A comprehensive module to manage a logistics company's fleet of vehicles, drivers, routes, and maintenance schedules.
    """,
    'sequence': 3,
    'author': "muhammadharoon26",
    'website': "https://muhammadharoon26.vercel.app",
    'category': 'Services/Fleet',
    'version': '18.0.1.0.0',
    'license': 'LGPL-3',
    'depends': ['base','fleet'],
    'data': [
        'security/ir.model.access.csv',
        'views/fleet_vehicle_search_views.xml',
        'views/fleet_vehicle_views.xml',
        'views/fleet_driver_views.xml',
        'views/menus.xml',
    ],
    'application': True,
    'installable': True,
}