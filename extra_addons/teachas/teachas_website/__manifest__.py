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
        'web'
    ],
    'data': [
        'security/ir.model.access.csv',
        'security/management_bug_security.xml',
        'views/management_bug.xml',
        'data/bugs_data.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
