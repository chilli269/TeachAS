from odoo import fields, models, api


class Days(models.Model):
    _name = "teachas.days"

    name = fields.Char(string="Day", required=True)
    mentori = fields.Many2many("res.users", "mentors_preferred_days", "preferred_days", "mentors", string="Mentors")
