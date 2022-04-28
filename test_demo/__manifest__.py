# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name' : 'Test',
    'version' : '1.2',
    'summary': 'Invoices & Payments',
    'sequence': 10,
    'description': """""",
    'category': 'Accounting/Accounting',
    'depends' : ['sale','mail'],
    'data': [

        'security/ir.model.access.csv',
        'views/views_test_demo.xml',
        'wizards/tast_demo_wizard_view.xml',
        # report
        'report/sale_report.xml',
        'report/test_demo_report.xml',
        'report/report_reg.xml',

    ],
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
}
