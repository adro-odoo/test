# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models


class StockMove(models.Model):
    _inherit = 'stock.picking'

    sale_type_id = fields.Many2one(
        'sale.type', string='Sales Type', readonly=True)
