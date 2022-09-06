from odoo import fields, models, api

class TeachAS(models.Model):
    _name = "teachas"

    materie = fields.Selection([('informatica', 'Informatică'), ('matematica', 'Matematică'), ('fizica', 'Fizică'), ('biologie', 'Biologie'), ('chimie', 'Chimie'), ('engleza', 'Engleză'),
    ('franceza', 'Franceză'), ('germana', 'Germană'), ('spaniola', 'Spaniolă'), ('latina', 'Latină'), ('romana', 'Română'), ('istorie', 'Istorie'), ('geografie', 'Geografie')], string="Materie", required=True)
    mentor = fields.Many2one('res.users', string="Mentor", required=True)
    elev = fields.Many2one('res.users', string="Elev", required=True)
    data = fields.Datetime(string="Meeting Date and Time", required=True)
    time_length = fields.Float(string = "Meeting Length(hours)", required=True)
    

