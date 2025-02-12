# -*- coding: utf-8 -*-
{
    'name': 'project management',
    'version': '18.0.0.1.0',
    'summary': 'Trial',
    'category': 'management',
    'description': """product management""",
    'license': 'LGPL-3',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/product_management_views.xml',
        # 'views/academic_month_views.xml',
        # 'views/academic_year_views.xml',
        # 'views/standard_views.xml',
    ],
    'application': True,
    'installable': True,
}
