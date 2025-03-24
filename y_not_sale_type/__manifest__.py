# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Y-Not Sale Type',
    'summary': 'Y-Not Sale Type',
    "version": "1.2",
    'website': 'https://www.odoo.com',
    'author': 'Odoo PS-IN',
    'description': """
        -TASK ID - 3083428
        -Create  a new model(Sale Type), fields, views, security, menu
        -Create a many2one field in account.move and add into form view and tree view
        -Create a many2one field in sale.order and add into form view, tree view, search view,
                and add in the filter and group by option
        -Create a many2one field in stock.picking and add into form view and tree view
        -Write two methods which update the value sale type field from sale order to invoice and
                stock
        - Task ID - 3440827
        - Pick & Pay - Auto trigger Email.
    """,
    'category': 'Custom Development',
    'depends': ['sale_management', 'stock', 'account'],
    'data': [
        'data/mail_template_data.xml',
        'data/size_report_data.xml',
        'security/ir.model.access.csv',
        'views/view_sale_type.xml',
        'views/view_sale_order.xml',
        'views/view_account_move.xml',
        'views/view_stock_picking.xml',
        'views/view_stock_report.xml',
        'report/invoice_label.xml',
    ],
    'license': 'LGPL-3',
    'installable': True,
    'auto_install': False,
    'application' : True,
}

