# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    sale_type_id_adro = fields.Many2one(
        'sale.type', string='Sales Type', compute='_compute_sale_type', store=True)
    total_order_qty = fields.Char(string="Total Order Quantity")

    @api.depends('sale_type_id', 'picking_ids', 'invoice_ids')
    def _compute_sale_type(self):
        for record in self.picking_ids:
            record.sale_type_id = self.sale_type_id
        for record in self.invoice_ids:
            record.sale_type_id = self.sale_type_id
