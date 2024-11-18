from odoo import models, fields, api,_
from datetime import datetime
import pytz
from odoo.exceptions import UserError

class MedicalInvestigation(models.Model):
    _name='medical.investigation'
    _description = 'Investigation'
    
    
    patient_id = fields.Many2one('medical.patient', string='Patient', help="Patient Name",select=True,required =True) 
    name = fields.Char("Name",related = patient_id.name)
    invest_info_ids = fields.One2many('investigation.info','invest_id',string="Information")
    inpatient_reg_id =fields.Many2one('medical.inpatient.registration',string='Inpatient Code', help="Patient Name",select=True)
    
    ecg=fields.Text("ECG")
    cxr=fields.Text("CXR")
    usg=fields.Text("USG")
    inv_others =fields.Text("Others")
 
    @api.model
    def create(self, vals):
        """Sequence number generation"""
        if vals.get('name', 'New') == 'New':
            patient = self.env['medical.patient'].browse(vals.get('patient_id'))
            vals['name'] = patient.name
        return super().create(vals)
 
    def action_print_investigation(self):
        
        return self.env.ref(
            'base_hms_customization.patient_investigation_pdf_reports'
        ).report_action(self)
        
        
