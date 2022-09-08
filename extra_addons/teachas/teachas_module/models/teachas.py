from odoo import fields, models, api

class TeachAS(models.Model):
    _name = "teachas"

    materie = fields.Many2one('teachas.subjects', string="Materie")
    mentor = fields.Many2one('res.users', string="Mentor")
    elev = fields.Many2one('res.users', string="Elev")
    data = fields.Datetime(string="Meeting Date and Time")
    time_length = fields.Float(string = "Meeting Length(hours)")


class Subjects(models.Model):
    _name = "teachas.subjects"

    name = fields.Char(string = "Subject/Materie", required = True)
    mentori = fields.One2many('res.users', 'materie', string = "Mentori", required = True)
    

