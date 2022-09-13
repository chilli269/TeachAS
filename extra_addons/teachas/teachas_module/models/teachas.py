from odoo import fields, models, api
from odoo.exceptions import UserError, ValidationError

class TeachAS(models.Model):
    _name = "teachas"

    materie = fields.Many2one('teachas.subjects', string="Materie")
    mentor = fields.Many2one('res.users', string="Mentor")
    elev = fields.Many2one('res.users', string="Elev")
    data = fields.Datetime(string="Meeting Date and Time")
    time_length = fields.Selection([('30m', '30 Minutes'),('1h', '1 Hour'),('1h30m', '1 Hour and 30 Minutes'),('2h', '2 Hours')], string="Time Length", default='30m')
    # hour_length=fields.Integer(string="Hours")
    # minute_length=fields.Integer(string="Minutes")
    is_session=fields.Boolean('Is Interactive Session?', default=False)

    @api.onchange('minute_length')
    def _check_minutes(self):
        if (self.minute_length>59):
            raise UserError('Your meeting time minutes cannot exceed 59')
    

