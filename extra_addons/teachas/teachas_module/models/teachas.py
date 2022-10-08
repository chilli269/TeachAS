from odoo import fields, models, api
from odoo.exceptions import UserError, ValidationError


class TeachAS(models.Model):
    _name = "teachas"

    materie = fields.Many2one('teachas.subjects', string="Materie", required=True)
    mentor = fields.Many2one('res.users', string="Mentor")
    elev = fields.Many2one('res.users', string="Elev")
    data = fields.Many2one('teachas.days', string="Date")
    time_length = fields.Selection(
        [('half', '30 Minutes'), ('hour', 'One Hour'), ('hourhalf', 'One Hour and 30 Minutes'),
         ('twohours', 'Two Hours')], 'Meeting duration', required=True)
    is_session = fields.Boolean('Is Interactive Session?', default=False)
    interactive_session_title = fields.Char(string="Presentation Title")
    session_type = fields.Selection([('online', 'Online'), ('fizic', 'Fizic'), ('other', 'I prefer not to say')],
                                    string="Session Type")
    details = fields.Text(string="Meeting Details")
    meeting_link = fields.Char(string="Meeting Link")

    mentor_check=fields.Boolean('Is checked by mentor', default=False)
    student_check=fields.Boolean('Is checked by student', default=False)

    stage_id=fields.Selection([('ongoing','Ongoing'),('done','Done')], default="ongoing")

    @api.onchange('mentor_check','student_check')
    def check_validity(self):
        if self.mentor_check and self.student_check:
            self.stage_id='done'
        else:
            self.stage_id='ongoing'

