# -*- coding: utf-8 -*-
{
    'name': "Worksheet Template QR Code Generator",
    'description': "Worksheet Template QR Code Generator",
    'odoo_task_id': "",
    'author': "Odoo PS-IN",
    'website': "https://www.odoo.com/",
    'version': '1.0',
    'depends': [
        'base_automation',
        'industry_fsm',
        'industry_fsm_report',
        'worksheet',
    ],
    'data': [
        'data/project_task_fields.xml',
        'data/base_automation.xml',
        'views/project_task_views.xml',
        'report/worksheet_template_report_template.xml',
        'report/project_task_reports.xml',
    ],

    'application': False,
    'installable': True,
    'auto_install': False,
    'license' : 'LGPL-3',
}

