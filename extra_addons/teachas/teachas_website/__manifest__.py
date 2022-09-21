# -*- coding: utf-8 -*-
{
    'name': "TeachAS Website",
    'description': """
        TeachAS website module for teachers/students to create and manage their events.
    """,
    'version': '1.0.0',
    'category': 'Website',
    'author': "Mihnea Grigore, Dennis Bart",
    'depends': [
        'base',
        'website',
        'web',
        'teachas_module'
    ],
    'data': [
        'views/dashboard_template.xml',
        'views/schedule_meeting_template.xml',
        'views/snippets/snippets.xml'
    ],
    'assets': {
        'web.assets_frontend': [
            'teachas_website/static/src/**/*.css',
            'teachas_website/static/src/js/teachas_snippet.js',
        ],
        'web.assets_backend': [
            
        ],
    },
    'installable': True,
    'application': True,
    'auto_install': False,
}
