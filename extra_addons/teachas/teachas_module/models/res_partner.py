from odoo import fields, models, api

class AddContactType(models.Model):
    _inherit = "res.partner"

    contact_type = fields.Selection([('elev', 'Elev'),('mentor', 'Mentor')], string="Contact Type", default='elev')