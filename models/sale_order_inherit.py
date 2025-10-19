from odoo import models, fields, api

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    # snapshot fields for receipt (optional: keep a copy independent of partner changes)
    receipt_customer_name = fields.Char(string='Customer Name', compute='_compute_customer_snapshot', store=True)
    receipt_address = fields.Char(string='Customer Address', compute='_compute_customer_snapshot', store=True)
    receipt_mobile = fields.Char(string='Customer Mobile', compute='_compute_customer_snapshot', store=True)

    # Example: link to purchase orders / receipts -- sale.order already has order_line; 
    # if you want to link to a purchase.order (supplier PO), add a Many2many/One2many accordingly.
    # Here we demonstrate a computed total for receipt and receipt number field:
    receipt_number = fields.Char(string='Receipt No.')
    receipt_total = fields.Monetary(string='Receipt Total', currency_field='currency_id', compute='_compute_receipt_total', store=True)

    @api.depends('partner_id', 'partner_id.name', 'partner_id.email', 'partner_id.phone', 'partner_id.mobile', 'partner_id.street', 'partner_id.city', 'partner_id.zip', 'partner_id.country_id')
    def _compute_customer_snapshot(self):
        for rec in self:
            if rec.partner_id:
                rec.receipt_customer_name = rec.partner_id.name or ''
                address_parts = []
                if rec.partner_id.street:
                    address_parts.append(rec.partner_id.street)
                if rec.partner_id.city:
                    address_parts.append(rec.partner_id.city)
                if rec.partner_id.zip:
                    address_parts.append(rec.partner_id.zip)
                if rec.partner_id.country_id:
                    address_parts.append(rec.partner_id.country_id.name or '')
                rec.receipt_address = ', '.join(address_parts)
                rec.receipt_mobile = rec.partner_id.mobile or rec.partner_id.phone or ''
            else:
                rec.receipt_customer_name = ''
                rec.receipt_address = ''
                rec.receipt_mobile = ''

    @api.depends('order_line.price_total')
    def _compute_receipt_total(self):
        for rec in self:
            rec.receipt_total = sum(line.price_total for line in rec.order_line) or 0.0
