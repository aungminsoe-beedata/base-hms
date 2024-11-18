from odoo import models, fields


class PatientRooms(models.Model):
    _name = 'hms_room.room'
    _description = 'Patient Rooms'

    name = fields.Char(string="Name", required=True, index=True, tracking=True)
    status = fields.Selection([
        ('availiable', 'Availiable'),
        ('occupies', 'Occupied'),

    ], string='Status', readonly=True, copy=False, index=True, tracking=True, default='availiable')

