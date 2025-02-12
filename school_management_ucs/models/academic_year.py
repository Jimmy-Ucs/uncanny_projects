from odoo import fields,models,_

class AcademicYear(models.Model):

    _name="academic.year"
    _description = "academic year"
    _rec_name = "name"

    name = fields.Char(string="student name")
    s_date = fields.Date(string="start date")
    st_date = fields.Date(string="stop date")
    c_year = fields.Boolean(string="is current Year ..?")
    description=fields.Text(string="describe")
    month_ids=fields.One2many("academic.month","year_id",string="Academic Month")
    subject=fields.Char(string="subject name")
    remarks=fields.Char(string="remarks of subject")
