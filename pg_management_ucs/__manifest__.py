# -*- coding: utf-8 -*-
{
    'name': 'Trial Module',
    'version': '18.0.0.1.0',
    'summary': 'Trial',
    'category': 'sale',
    'description': """Trial module""",
    'license': 'LGPL-3',
    'depends': ['base', 'sale_management'],
    'data': [
        'security/ir.model.access.csv',
        'views/trial_module_views.xml'
    ],
    'application': True,
    'installable': True,
}
