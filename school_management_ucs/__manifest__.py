# -*- coding: utf-8 -*-
{
    'name': 'School management',
    'version': '18.0.0.1.0',
    'summary': 'Trial',
    'category': 'management',
    'description': """school management""",
    'license': 'LGPL-3',
    'depends': ['base', 'sale'],
    'data': [
        'security/ir.model.access.csv',
        'security/principal_security.xml',
        'views/school_management_views.xml',
        'views/academic_month_views.xml',
        'views/academic_year_views.xml',
        'views/standard_views.xml',
        'wizard/student_data_wizard_views.xml',
    ],
    'application': True,
    'installable': True,
}
