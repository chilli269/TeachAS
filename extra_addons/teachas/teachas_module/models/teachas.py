from odoo import fields, models, api
from odoo.exceptions import UserError, ValidationError

class TeachAS(models.Model):
    _name = "teachas"

    materie = fields.Many2one('teachas.subjects', string="Materie", required=True)
    mentor = fields.Many2one('res.users', string="Mentor")
    elev = fields.Many2one('res.users', string="Elev")
    data = fields.Datetime(string="Meeting Date and Time")
    # time_length = fields.Float(string = "Meeting Length(hours)")
    time_length=fields.Selection([('half','30 Minutes'),('hour','One Hour'),('hourhalf','One Hour and 30 Minutes'),('twohours','Two Hours')],'Meeting duration', required=True)
    # hour_length=fields.Integer(string="Hours")
    # minute_length=fields.Integer(string="Minutes")
    is_session=fields.Boolean('Is Interactive Session?', default=False)

    @api.onchange('minute_length')
    def _check_minutes(self):
        if (self.minute_length>59):
            raise UserError('Your meeting time minutes cannot exceed 59')
    

