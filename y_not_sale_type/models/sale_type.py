# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models


class SaleType(models.Model):
    _name = 'sale.type'
    _description = 'Sale Type'

    name = fields.Char(string='Sale Type')
    auto_email_invoice_post = fields.Boolean(string='Auto Mail')
