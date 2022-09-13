from odoo import fields, models, api

class Subjects(models.Model):
    _name = "teachas.subjects"

    name = fields.Char(string = "Subject/Materie", required = True)
    mentori = fields.One2many('res.users', 'materie', string = "Mentori", required = True)