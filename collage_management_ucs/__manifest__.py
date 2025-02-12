# -*- coding: utf-8 -*-
{
    'name': 'customer management',
    'version': '18.0.0.1.0',
    'summary': 'Trial',
    'category': 'sale',
    'description': """customer management""",
    'license': 'LGPL-3',
    'depends': ['base', 'sale'],
    'data': [
        'security/ir.model.access.csv',
        'views/collage_management_views.xml',
        'wizard/collage_management_wizard_views.xml',

    ],
    'application': True,
    'installable': True,
}
