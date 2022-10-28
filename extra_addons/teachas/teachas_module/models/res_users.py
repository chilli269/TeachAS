from odoo import fields, models, api

from datetime import datetime

import logging
_logger = logging.getLogger(__name__)

class AddContactType(models.Model):
    _inherit = "res.users"

    contact_type = fields.Selection([('elev', 'Elev'),('mentor', 'Mentor'),('other', 'Other')], string="Contact Type", default='elev')
    materie = fields.Many2many('teachas.subjects', 'mentors_subjects', 'mentors', 'subjects', string="Materie mentor")
    preferred_days = fields.Many2many("teachas.days", "mentors_preferred_days", "mentors", "preferred_days", string="Preferred Days")
    available_hours = fields.Float(string="Available Weekly Hours")
    phone_number = fields.Char(string="Phone Number")
    exp_points = fields.Float('Experience points', default=0) #readonly=True,need to make it readonly after calculation is implemented
    grade_id = fields.Selection([('1','5th-8th'),('2', '9th'),('3', '10th'),('4', '11th'),('5','12th')], string="Grade")

    auxiliary_hours=fields.Float(default=0)

    @api.model
    def _available_hours_reset(self):

        _logger.info('\n\n ASDASDASDASDAS \n\n')
        if datetime.today().weekday()==6:
            _logger.info('\n\n ok oksoakooa \n\n')
            self.available_hours+=self.auxiliary_hours
            self.auxiliary_hours=0
        