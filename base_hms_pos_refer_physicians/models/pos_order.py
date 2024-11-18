# -*- coding: utf-8 -*-
################################################################################

################################################################################
from odoo import fields, models


class PosOrderLine(models.Model):
    """ The class PosOrder is used to inherit pos.order.line """
    _inherit = 'pos.order.line'

    physician_id = fields.Many2one('medical.physician', string='Physicians',
                              help="You can see Physicians here")
    
    referral_payment_status = fields.Selection([
        ('pending', 'Pending'),
        ('done', 'Done'),
    ], string='Referral Paid',default="pending")
    date = fields.Datetime(string="Date", related='order_id.date_order', store=True)
