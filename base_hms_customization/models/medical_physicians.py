from odoo import models, fields, api, _
from odoo.exceptions import ValidationError
import re

class MedicalPhysician(models.Model):
    _inherit = "medical.physician"
    
    phone = fields.Char("Phone")
    
    def _compute_bill_count(self):
        self.referred_bill_count = len(self.referred_bill_ids)

    refer_percentage = fields.Float(string="Refer Percent")
    referred_bill_ids = fields.One2many('account.move', 'referral_physician_id', string="Bills")
    referred_bill_count = fields.Integer(string="Bill Count", compute=_compute_bill_count)

    def action_view_vendor_bill(self):
        self.ensure_one()
        result = {
            "type": "ir.actions.act_window",
            "res_model": "account.move",
            "domain": [('id', 'in', self.referred_bill_ids.ids), ('move_type', 'in', self.env['account.move'].get_purchase_types())],
            "context": {"create": False},
            "name": "Vendor Bills",
            'view_mode': 'tree,form',
        }
        return result

    def action_compute_referral(self):
        action = self.env['ir.actions.act_window']._for_xml_id('base_hms_customization.referral_payment_wizard_action')
        ctx = dict(self.env.context)
        ctx.pop('active_id', None)
        ctx['active_id'] = self.id
        ctx['active_model'] = 'medical.physician'
        action['context'] = ctx
        return action