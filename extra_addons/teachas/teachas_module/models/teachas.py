from odoo import fields, models, api

class TeachAS(models.Model):
    _name = "teachas"

    materie = fields.Many2one('teachas.subjects', string="Materie", required=True)
    mentor = fields.Many2one('res.users', string="Mentor", required=True)
    elev = fields.Many2one('res.users', string="Elev", required=True)
    data = fields.Datetime(string="Meeting Date and Time", required=True)
    time_length = fields.Float(string = "Meeting Length(hours)", required=True)


class Subjects(models.Model):
    _name = "teachas.subjects"

    name = fields.Char(string = "Subject/Materie", required = True)
    mentori = fields.One2many('res.users', 'materie', string = "Mentori", required = True)
    

