from odoo import fields, models, api

class Subjects(models.Model):
    _name = "teachas.subjects"

    name = fields.Char(string = "Subject/Materie", required = True)
    mentori = fields.Many2many('res.users', 'mentors_subjects', 'subjects', 'mentors', string = "Mentori", required = True)