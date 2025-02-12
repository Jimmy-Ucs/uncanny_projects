from odoo import models, fields, api



class LibraryCard(models.Model):
    _name = "library.card"
    _description = "Library Author"
    _rec_name = "user"

    code = fields.Char(string="", required=True)
    disciplinary_action = fields.Char(string="")
    remarks = fields.Char(string="")
    book_limit = fields.Integer(string="")
    student = fields.Many2one('res.partner', string="student")
    card = fields.Char(string="card")
    user = fields.Selection([
        ('student', 'Student'),
        ('teacher', 'Teacher'),
        ('staff', 'Staff')
    ], string="User")
    active = fields.Boolean(string="Is the field active", default="True")
    startdate = fields.Date(string="startdate")
    enddate = fields.Date(string="enddate")

