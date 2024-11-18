from odoo import models, fields, api


class operation_note(models.Model):
    _name = 'operation.note'
    _description = 'operation_note'

    patient_id = fields.Many2one('medical.patient', string='Patient', help="Patient Name",select=True,required=True)
    name = fields.Char("Name",related = patient_id.name)  
    inpatient_reg_id =fields.Many2one('medical.inpatient.registration',string='Patient', help="Patient Name",select=True)

    @api.model
    def create(self, vals):
        """Sequence number generation"""
        if vals.get('name', 'New') == 'New':
            patient = self.env['medical.patient'].browse(vals.get('patient_id'))
            vals['name'] = patient.name
        return super().create(vals)

   
    note=fields.Text(string="Note")
    diagnosis =fields.Text(string="Diagnosis")
    operation_types=fields.Text(string="Types Of Operation Performed")
    surgeon =fields.Char(string="Surgeon")
    anaesthetist=fields.Char(string="Anaesthetist")
    paediatrician=fields.Char(string="Paediatrician")
    assistant_1st =fields.Char(string="1st Assistant")
    assistant_2nd = fields.Char(string="2nd Assistant")
    instrument_nurse=fields.Char(string="Instrument Nurse")
    procedure_findings=fields.Text(string="PROCEDURE & FINDINGS")
    advise=fields.Text(string="Advise")
    
    def print_operation_notes(self):
        return self.env.ref(
            'base_hms_customization.patient_operation_notes_pdf_reports'
        ).report_action(self)
        
        
