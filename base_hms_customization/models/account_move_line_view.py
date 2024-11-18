# -*- coding: utf-8 -*-

from odoo import models, fields


class AccountMove(models.Model):
    _inherit = "account.move"

    referral_physician_id = fields.Many2one('medical.physician', string="Referral Physician")


class AccountMoveLine(models.Model):
    _inherit = "account.move.line"

    physician_id = fields.Many2one('medical.physician', string="Refer Physician")
    referral_payment_status = fields.Selection([
        ('pending', 'Pending'),
        ('done', 'Done'),
    ], string='Referral Paid')
