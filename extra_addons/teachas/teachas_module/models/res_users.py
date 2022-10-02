from odoo import fields, models, api

class AddContactType(models.Model):
    _inherit = "res.users"

    contact_type = fields.Selection([('elev', 'Elev'),('mentor', 'Mentor'),('other', 'Other')], string="Contact Type", default='elev')
    materie = fields.Many2one('teachas.subjects', string="Materie mentor")
    preferred_days = fields.Many2many("teachas.days", "mentors_preferred_days", "mentors", "preferred_days", string="Preferred Days")
    available_hours = fields.Float(string="Available Weekly Hours")
    phone_number = fields.Char(string="Phone Number")
    exp_points = fields.Float('Experience points', default=0) #readonly=True,need to make it readonly after calculation is implemented
    grade_id = fields.Selection([('8','5th-8th'),('9', '9th'),('10', '10th'),('11', '11th'),('12','12th')], string="Grade")