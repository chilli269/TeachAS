from odoo import fields, models, api

class AddContactType(models.Model):
    _inherit = "res.users"

    contact_type = fields.Selection([('elev', 'Elev'),('mentor', 'Mentor'),('other', 'Other')], string="Contact Type", default='elev')
    materie = fields.Many2one('teachas.subjects', string="Materie mentor")
    preferred_days = fields.Many2many("teachas.days", "mentors_preferred_days", "mentors", "preferred_days", string="Preferred Days")
    available_hours = fields.Float(string="Available Weekly Hours")
    phone_number = fields.Char(string="Phone Number")