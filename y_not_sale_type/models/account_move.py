# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models, _
import base64

class AccountMove(models.Model):
    _inherit = 'account.move'

    sale_type_id = fields.Many2one(
        'sale.type', string='Sales Type', readonly=True)

    def _send_mail_on_confirm_invoice(self):
        template = self.env.ref('y_not_sale_type.email_template_invoice_delivery_ynotdesign', raise_if_not_found=False)
        sale_order_id = self.env['sale.order'].search([('invoice_ids', '=', self.id)], limit=1)
        picking_id = sale_order_id.picking_ids[0] if sale_order_id.picking_ids else False
        #Delivery Slip
        report_delivery = self.env.ref('stock.action_report_delivery', False)
        pdf_content_delivery, content_type_delivery = self.env["ir.actions.report"]._render_qweb_pdf(report_delivery, res_ids=picking_id.id)
        delivery_name = _('Delivery Slip - %s - %s', self.partner_id.name or '', picking_id.name)
        #Invoice Slip
        report_invoice = self.env.ref('account.account_invoices', False)
        pdf_content_invoice, content_type_invoice = self.env["ir.actions.report"]._render_qweb_pdf(report_invoice, res_ids=self.id)
        invoice_name = self._get_move_display_name() or "invoice slip"
        #Invoice Label
        report_invoice_label = self.env.ref('y_not_sale_type.action_report_invoice_label', False)
        pdf_content_invoice_label, content_type_invoice_label = self.env["ir.actions.report"]._render_qweb_pdf(report_invoice_label, res_ids=self.id)
        invoice_label_name = "invoice label slip"

        attachment_vals = [
            {
                'name': invoice_name,
                'type': 'binary',
                'datas': base64.encodebytes(pdf_content_invoice),
                'res_model': self._name,
                'res_id': self.id
            },
            {
                'name': delivery_name,
                'type': 'binary',
                'datas': base64.encodebytes(pdf_content_delivery),
                'res_model': self._name,
                'res_id': self.id
            },
            {
                'name': invoice_label_name,
                'type': 'binary',
                'datas': base64.encodebytes(pdf_content_invoice_label),
                'res_model': self._name,
                'res_id': self.id
            }
        ]
        attachments = self.env['ir.attachment'].create(attachment_vals)
        if template:
            email_values = {
                'attachment_ids': attachments,
            }
            template.send_mail(
                self.id,
                email_values=email_values,
                email_layout_xmlid='mail.mail_notification_light',
                force_send=True)

    def _post(self, soft=True):
        res = super()._post(soft)
        if self.sale_type_id.auto_email_invoice_post:
            self._send_mail_on_confirm_invoice()
        return res
