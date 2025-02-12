from odoo import models, fields, api

class Library(models.Model):
    _name = "library"
    _description = "Library management system"

    name = fields.Char(string="The name of the author")
    birthdate = fields.Date(string="birthdate")
    deathdate = fields.Date(string="deathdate")
    biography = fields.Text(string="Biography")
    note = fields.Text(string="note")
    code = fields.Char(string="Code of the rack")
    active = fields.Boolean(string="Is the field active", default="True")

    editor = fields.Many2many('res.partner', string='Editors name')




