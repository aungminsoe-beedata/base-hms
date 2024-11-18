from odoo import models, fields, api,_


class MedicalPatientHospital(models.Model):
    _inherit = 'medical.patient'
    _description = 'Medical Patient Inherit'
    
    father_name=fields.Char("Father Name", store=True)
    state = fields.Selection([
        ('draft', 'Free'),
        ('done', 'Hospitalized'),
    ], string='Patient Status', readonly=True, copy=False, index=True, tracking=True, default='draft')
  
    
    # status_patient = fields.Selection([
    #     ('attend', 'Attending'),
    #     ('out', 'Out Patient'),
   
    def _investigation_count(self):
        for patient in self:
            patient.investigation_count = len(patient.investigation_ids)
        return True

    investigation_ids = fields.One2many('medical.investigation', 'patient_id', string='Investigation')
    investigation_count = fields.Integer(compute=_investigation_count, string="Investigation")
    
    
    def _operation_notes_count(self):
        for patient in self:
            patient.operation_notes_count = len(patient.operation_notes_ids)
        return True
    operation_notes_ids = fields.One2many('operation.note', 'patient_id', string='Operation Notes')
    operation_notes_count = fields.Integer(compute=_operation_notes_count,string="Operation Notes")
    
    
    
    def _patient_hosptializaton_count(self):
        for patient in self:
            patient.patient_hosptializaton_count = len(patient.patient_hosptialization)
        return True
    patient_hosptialization = fields.One2many('medical.inpatient.registration', 'patient_id', string='Operation Notes')
    patient_hosptializaton_count = fields.Integer(compute=_patient_hosptializaton_count,string="Patient Hospitalization")



  
    def action_get_investigation(self):
        self.ensure_one()
        return {
            
            'name': _('Investigation'),
            'view_type': 'tree',
            'view_mode': 'list,form',
            'res_model': 'medical.investigation',
            'type': 'ir.actions.act_window',
            'context': self.env.context,
            'domain': [('patient_id', '=', self.id)],
           
        }


        
    def action_get_operations_notes(self):
        
        self.ensure_one()
        return {
            'type': 'ir.actions.act_window',
            'name': _('Operation Notes'),
            'view_type': 'tree',
            'view_mode': 'list,form',
            'res_model': 'operation.note',
            'context': self.env.context,
            'domain': [('patient_id', '=', self.id)],
            
        }


        
        