# -*- coding: utf-8 -*-
{
    'name': 'Zomato management',
    'version': '18.0.0.1.0',
    'summary': 'Trial',
    'category': 'sale',
    'description': """Zomato management""",
    'license': 'LGPL-3',
    'depends': ['sale_management', 'base'],
    'data': [
        'security/ir.model.access.csv',
        'views/zomato_management_views.xml',
    ],
    'application': True,
    'installable': True,
}
