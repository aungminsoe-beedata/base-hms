# -*- coding: utf-8 -*-

from odoo import models, fields


class ProductCategory(models.Model):
    _inherit = "product.category"

    is_refer = fields.Boolean('Is Refer', default=True)
    refer_percent = fields.Float(string='Refer (%)', digits='Discount', default=10.0)