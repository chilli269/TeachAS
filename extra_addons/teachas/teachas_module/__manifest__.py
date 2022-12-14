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
        'contacts',
        'mail',
        'contacts'
    ],
    'data': [
        'security/ir.model.access.csv',
        'data/ir_cron_data.xml',
        'data/email_templates.xml',
        'views/res_users.xml',
        'views/teachas.xml'
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
