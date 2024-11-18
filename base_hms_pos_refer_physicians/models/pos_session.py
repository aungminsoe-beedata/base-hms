# -*- coding: utf-8 -*-
################################################################################

################################################################################
from odoo import models


class PosSession(models.Model):
    """The class PosSession is used to inherit pos.session"""
    _inherit = 'pos.session'

    def load_pos_data(self):
        """Load POS data and add `res_users` to the response dictionary.
        return: A dictionary containing the POS data.
        """
        res = super().load_pos_data()
        res['employee_casher_user'] = self.env['medical.physician'].search_read(fields=['partner_id'])
        return res
