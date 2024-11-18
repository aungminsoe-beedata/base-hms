from odoo import models, fields, api,_
from datetime import datetime
import pytz
from odoo.exceptions import UserError

class InvestigationInfo(models.Model):
    _name='investigation.info'
    _description = 'Investigation Info'
    date = fields.Date(string="Date",required =True)
    invest_id=fields.Many2one('medical.investigation')
    hb=fields.Char(string="HB",help="Hemoglobin (Hb) is the protein contained in red blood cells that is responsible for delivery of oxygen to the tissues. To ensure adequate tissue oxygenation, a sufficient hemoglobin level must be maintained.")
    mcv=fields.Char(string="MCV",help="The mean corpuscular volume (MCV) is a critical measurement for identifying the underlying cause of anemia. MCV is a laboratory value that measures the average size and volume of red blood cells (RBCs), providing essential information in the diagnostic process for anemia. MCV is expressed as femtoliters (fL)")
    wbc=fields.Char(string="WBC",help="What is a white blood count (WBC)? A white blood count measures the number of white blood cells (WBCs) in your blood. White blood cells, also called leukocytes, are part of your immune system. They are a type of blood cell made in your bone marrow and found in your blood and lymph tissue (part of your immune system).")
    anc=fields.Char(string="ANC",help="What is absolute neutrophil count? The absolute neutrophil count (ANC) is an estimate of the body's ability to fight infections, especially bacterial infections.")
    plt=fields.Char(string="PLT",help="")
    crp=fields.Char(string="CRP")
    esr =fields.Char("ESR")
    urea=fields.Char("Urea")
    creatinine=fields.Char("Creatinine")
    egfr=fields.Char("eGFR")
    na=fields.Char("Na")
    k=fields.Char("K")
    hco3=fields.Char("HCO3")
    t_dp= fields.Char("T & DP")
    albumin =fields.Char("Albumin")
    ast = fields.Char("AST")
    alt = fields.Char("ALT")
    alk_phos=fields.Char("Alk Phos")
    pt= fields.Char("PT")
    inr=fields.Char("INR")
    aptt = fields.Char("APTT")
    rbs= fields.Char("RBS")
    hba1_c =fields.Char("HbA 1 C",help="What is a hemoglobin A1C (HbA1C) test? A hemoglobin A1C (HbA1C) test is a blood test that shows what your average blood sugar (glucose) level was over the past two to three months. Glucose is a type of sugar in your blood that comes from the foods you eat.")
    t_3 = fields.Char("T3")
    t_4 = fields.Char("T4")
    tsh=fields.Char("TSH")
    cho=fields.Char("Cho")
    tg=fields.Char("TG")
    hdl=fields.Char('HDL')
    ldl=fields.Char("LDL")
