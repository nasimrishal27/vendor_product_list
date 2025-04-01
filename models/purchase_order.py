# -*- coding: utf-8 -*-
from odoo import api, fields, models


class PurchaseOrder(models.Model):
    _inherit = "purchase.order"

    is_vendor_products = fields.Boolean(string="Vendor Product")

    @api.onchange('is_vendor_products')
    def _onchange_is_vendor_products(self):
        if self.is_vendor_products:
            print("Haaaiii")
            # self.order_line.product_id = self.env['product.product'].search([('seller_ids.partner_id.id', '=', self.partner_id.id)])
            print(self.env['product.product'].search([('seller_ids.partner_id.id', '=', self.partner_id.id)]))
        else:
            print('HElllooi')