from odoo import fields, models, api

class AddContactType(models.Model):
    _inherit = "res.users"

    contact_type = fields.Selection([('elev', 'Elev'),('mentor', 'Mentor'),('other', 'Other')], string="Contact Type", default='elev')