# -*- coding: utf-8 -*-
from odoo import api, fields, models
from itertools import groupby
from odoo.exceptions import ValidationError


class ReferralPaymentWizard(models.TransientModel):
    _name = "referral.payment.wizard"
    _description = "Referral Physician Payment"

    @api.onchange('date', 'physician_id')
    def _get_referral_lines(self):
        domain = [
            ('date', '<=', self.date),
            ('referral_payment_status', '=', 'pending'),
            ('physician_id', '=', self.env.context.get('active_id'))
        ]
        
        domain1 = [
            ('date', '<=', self.date),
            ('order_id.state', '=', 'paid'),
            ('referral_payment_status', '=', 'pending'),
            ('physician_id', '=', self.env.context.get('active_id'))
        ]
        self.pos_order_line_ids = self.env['pos.order.line'].search(domain1)
        self.account_move_line_ids = self.env['account.move.line'].search(domain)

    @api.onchange('pos_order_line_ids', 'account_move_line_ids')
    def _compute_vendor_bill_data(self):
        domain = [('company_id', '=', self.env.company.id), ('type', '=', 'purchase')]
        self.journal_id = self.env['account.journal'].search(domain, limit=1)

        group_pos_line_by_currency = {k: v for k, v in groupby(
            sorted(self.pos_order_line_ids, key=lambda x: x.currency_id), lambda x: x.currency_id)}
        group_account_move_line_by_currency = {k: v for k, v in groupby(
            sorted(self.account_move_line_ids, key=lambda x: x.currency_id), lambda x: x.currency_id)}
        if len(group_pos_line_by_currency) > 1 or len(group_account_move_line_by_currency) > 1:
            raise ValidationError('Multi Currencies not supported for now')
        elif group_pos_line_by_currency and group_account_move_line_by_currency:
            if next(iter(group_pos_line_by_currency)) != next(iter(group_account_move_line_by_currency)):
                raise ValidationError('Multi Currencies not supported for now')
        self.currency_id = next(iter(group_pos_line_by_currency)) if group_pos_line_by_currency \
            else next(iter(group_account_move_line_by_currency)) if group_account_move_line_by_currency else None

        self.total_referral_amount = sum(
            pos_line.price_subtotal_incl * pos_line.product_id.categ_id.refer_percent / 100 for pos_line in
            self.pos_order_line_ids) + \
                                     sum(move_line.price_subtotal * move_line.product_id.categ_id.refer_percent / 100
                                         for move_line in self.account_move_line_ids)

    def get_referral_product(self):
        return self.env.user.company_id.referral_payment_product_id

    date = fields.Date(string='Date', default=lambda self: fields.Date.context_today(self), required=True)
    journal_id = fields.Many2one('account.journal', string="Journal", required=True, compute=_compute_vendor_bill_data)

    pos_order_line_ids = fields.Many2many('pos.order.line', string="POS", compute=_get_referral_lines)
    account_move_line_ids = fields.Many2many('account.move.line', string="Sales", compute=_get_referral_lines)

    currency_id = fields.Many2one('res.currency', string='Currency', required=True, compute=_compute_vendor_bill_data)
    total_referral_amount = fields.Float(string="Total", compute=_compute_vendor_bill_data)
    
    
    def get_product_account(self):
        accounts = self.get_referral_product().product_tmpl_id.get_product_accounts()
        return accounts['expense']
    
    def _prepare_invoice_vals(self):
        return {
            'partner_id': self.env['medical.physician'].browse(self.env.context.get('active_id')).partner_id.id,
            'move_type': 'in_invoice',
            'invoice_origin': "Referral Payment till {date}".format(date=self.date),
            'journal_id': self.journal_id.id,
            'currency_id': self.currency_id.id,
            'invoice_date': self.date,
            'referral_physician_id': self.env.context.get('active_id'),
            'invoice_line_ids': [
                (0, 0, {
                    'product_id': self.get_referral_product().id,
                    'name': "Referral Payment till {date}".format(date=self.date),
                    'account_id': self.get_product_account().id,
                    'quantity': '1',
                    'price_unit': self.total_referral_amount,
                    'product_uom_id': self.get_referral_product().uom_id.id,
                })
            ]
        }
    def check_referral_product(self):
        if not self.env.user.company_id.referral_payment_product_id:
            raise ValidationError('Referral Product is needed to be configured!.')

    def change_referral_state_to_done(self):
        pass

    def create_payment(self):
        self.check_referral_product()
        create_bill = self.env['account.move'].create(self._prepare_invoice_vals())
        for pos_line in self.pos_order_line_ids:
            pos_line.referral_payment_status = 'done'
        for account_move_line in self.account_move_line_ids:
            account_move_line.referral_payment_status = 'done'


  