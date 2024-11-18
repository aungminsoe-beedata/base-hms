from odoo import fields, models


class PosOrderLine(models.Model):
    """ The class PosOrder is used to inherit pos.order.line """
    _inherit = 'pos.order.line'

    physician_id = fields.Many2one("medical.physician", string="Refer Physicians One")

    # def _prepare_invoice_line(self, **optional_values):
    #     res = super(SaleOrderLine, self)._prepare_invoice_line(**optional_values)
    #     res['physician_id'] = self.physician_id.id
    #     res['referral_payment_status'] = 'pending' if self.physician_id else None
    #     return res