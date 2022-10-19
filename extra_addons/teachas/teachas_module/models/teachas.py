from odoo import fields, models, api
from odoo.exceptions import UserError, ValidationError

import logging
_logger = logging.getLogger(__name__)


class TeachAS(models.Model):
    _name = "teachas"

    materie = fields.Many2one('teachas.subjects', string="Materie", required=True)
    mentor = fields.Many2one('res.users', string="Mentor")
    elev = fields.Many2one('res.users', string="Elev")
    data = fields.Many2one('teachas.days', string="Date")
    time_length = fields.Selection(
        [('half', '30 de minute'), ('hour', '1 oră'), ('hourhalf', '1 oră si 30 de minute'),
         ('twohours', '2 ore')], 'Meeting duration', required=True)
    is_session = fields.Boolean('Is Interactive Session?', default=False)
    interactive_session_title = fields.Char(string="Presentation Title")
    session_type = fields.Selection([('online', 'Online'), ('fizic', 'Fizic'), ('other', 'I prefer not to say')],
                                    string="Session Type")
    details = fields.Text(string="Meeting Details")
    meeting_link = fields.Char(string="Meeting Link")

    validity_check=fields.Integer(default=0)

    stage_id=fields.Selection([('ongoing','Ongoing'),('done','Done')], default="ongoing")

    @api.model
    def create(self, vals):
        res = super(TeachAS, self).create(vals)
        template = self.env.ref('teachas_module.email_template_schedule_success')
        _logger.info("\n\n dsadadadasdadad %s", template)
        _logger.info("\n\n dsadadadasdadad %s", res.id)
        template.sudo().send_mail(res.id ,force_send=True)
        _logger.info("\n\n email send \n\n %s")
        return res

