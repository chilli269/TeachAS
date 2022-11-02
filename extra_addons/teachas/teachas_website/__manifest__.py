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
        'teachas_module',
    ],
    'data': [
        'views/dashboard_template.xml',
        'views/schedule_meeting_template.xml',
        'views/snippets/snippets.xml',
        'views/gdpr.xml',
        'data/login.xml',
        'data/register.xml',
        'data/snippet_data.xml',
    ],
    'assets': {
        'web.assets_frontend': [
            'teachas_website/static/src/css/*.css',
            'teachas_website/static/src/js/teachas_snippet.js',
            'teachas_website/static/src/js/teachas_dashboard.js',
            'teachas_website/static/src/js/teachas_schedule.js',
        ],
        'web.assets_backend': [

        ],
    },
    'installable': True,
    'application': True,
    'auto_install': False,

    # UPON INSTALLATION, CONFIGURATION OF IR.CRON IS NECESSARY
    # ALSO, WHEN SETTING UP TEACHAS DAYS, BEGIN WITH MONDAY AND END WITH SUNDAY, IN THE USUAL ORDER
}
