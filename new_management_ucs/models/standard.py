from odoo import fields,models,_

class Standard(models.Model):
    _name="standard"
    _description = "academic month"
    _rec_name = "name"

    sequence=fields.Integer(string="Standard of student")
    name = fields.Char(string="student name")
    code = fields.Char(string="student EN. no.")
    desc = fields.Text(string="student description")
    subject=fields.Char(string="subject name")
    remarks=fields.Char(string="remarks of subject")

