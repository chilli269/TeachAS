# -*- coding: utf-8 -*-
{
    'name': "TeachAS Management Module",
    'description': """
        Manage your teachas resources, from teachers to students, their meetings, events.
    """,
    'version': '1.0.0',
    'category': '',
    'author': "Mihnea Grigore, Dennis Bart",
    'depends': [
        'base',
        'website',
        'web',
        'contacts'
    ],
    'data': [
        'views/res_partner.xml'
    ],
    'assets': {
        'web.assets_frontend': [
            
        ],
        'web.assets_backend': [
            
        ],
    },
    'installable': True,
    'application': True,
    'auto_install': False,
}
