from odoo import fields, models, api

class TeachAS(models.Model):
    _name = "teachas"

    materie = fields.Selection([('informatica', 'Informatică'), ('matematica', 'Matematică'), ('fizica', 'Fizică'), ('biologie', 'Biologie'), ('chimie', 'Chimie'), ('engleza', 'Engleză'),
    ('franceza', 'Franceză'), ('germana', 'Germană'), ('spaniola', 'Spaniolă'), ('latina', 'Latină'), ('romana', 'Română'), ('istorie', 'Istorie'), ('geografie', 'Geografie')], string="Materie")
    mentor = fields.Many2one('res.partner', string="Mentor")
    elev = fields.Many2one('res.partner', string="Elev")
    data = fields.Datetime(string="Meeting Date and Time")
    

