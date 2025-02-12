from odoo import models, fields, api

class LibraryRack(models.Model):
    _name = "library.rack"
    _description = "Library Rack"
    _rec_name = 'code'

    name = fields.Char(string="The name of the rack")
    code = fields.Char(string="Code of the rack")
    active = fields.Boolean(string="Is the field active" , default = "True")
