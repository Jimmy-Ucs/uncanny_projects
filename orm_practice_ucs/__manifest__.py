# -*- coding: utf-8 -*-
{
    'name': 'orm practice',
    'version': '18.0.0.1.0',
    'summary': 'Trial',
    'category': 'management',
    'description': """orm practice""",
    'license': 'LGPL-3',
    'depends': ['base','sale'],
    'data': [
        'security/ir.model.access.csv',
        'views/orm_practice_views.xml',
    ],
    'application': True,
    'installable': True,
}
