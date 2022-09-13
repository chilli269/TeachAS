from odoo import fields, models, api
from odoo.exceptions import UserError, ValidationError

class TeachAS(models.Model):
    _name = "teachas"

    materie = fields.Many2one('teachas.subjects', string="Materie")
    mentor = fields.Many2one('res.users', string="Mentor")
    elev = fields.Many2one('res.users', string="Elev")
    data = fields.Datetime(string="Meeting Date and Time")
    # time_length = fields.Float(string = "Meeting Length(hours)")
    hour_length=fields.Integer(string="Hours")
    minute_length=fields.Integer(string="Minutes")

    @api.onchange('minute_length')
    def _check_minutes(self):
        if (self.minute_length>60):
            raise UserError('Your meeting time minutes cannot exceed 60')
    

