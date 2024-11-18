# -*- coding: utf-8 -*-

from odoo import fields, models


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    referral_payment_product_id = fields.Many2one(
        'product.product',
        related='company_id.referral_payment_product_id',
        string="Product",
        readonly=False
    )
