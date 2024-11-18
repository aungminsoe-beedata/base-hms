# -*- coding: utf-8 -*-
from odoo import models, fields

class ResCompany(models.Model):
    _inherit = "res.company"

    referral_payment_product_id = fields.Many2one(
        'product.product', 
        string="Referral Payment Product",
        help="The product used for referral payments."
    )
