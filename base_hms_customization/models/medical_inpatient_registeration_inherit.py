from odoo import models, fields, api, _
from datetime import date,datetime

class medical_inpatient_registration(models.Model):
    _inherit = 'medical.inpatient.registration'

    patient_id = fields.Many2one('medical.patient',string="Patient",required=True ,domain="[('state', '=', 'draft')]")
    room_id = fields.Many2one('hms_room.room', string="Room", required=True, domain="[('status', '=', 'availiable')]")
    # status_patient = fields.Selection([
    #     ('attend', 'Attending'),
    #     ('out', 'Out Patient'),

    # ], string='Status', readonly=True, copy=False, index=True, tracking=True, default='availiable')

    @api.model
    def create(self,val):
        
        patient_id  = self.env['ir.sequence'].next_by_code('medical.inpatient.registration')
        if patient_id:
            val.update({
                        'name':patient_id,
                       })
        result = super(medical_inpatient_registration, self).create(val)
        return result

    def registration_admission(self):
        super(medical_inpatient_registration, self).registration_admission()
        for rec in self.room_id:
            rec.write({'status': 'occupies'})
        for rec in self.patient_id:
            rec.write({'state' : 'done'})

    def patient_discharge(self):
        super(medical_inpatient_registration, self).patient_discharge()
        for rec in self.room_id:
            rec.write({'status': 'availiable'})
        for rec in self.patient_id:
            rec.write({'state' : 'draft'})
