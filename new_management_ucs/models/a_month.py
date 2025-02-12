from odoo import api,fields,models,_
from wheel.cli.pack import compute_tagline


class AcademicMonth(models.Model):

    _name = "academic.month"
    _description = "academic month"
    _rec_name = "name"


    s_date = fields.Date(string="start date")
    st_date = fields.Date(string="stop date")
    c_year = fields.Boolean(string="is current Year ..?")
    description = fields.Text(string="describe")
    year_id = fields.Many2one("academic.year",string="academic year")
    name = fields.Char(related="year_id.name",string="student name")
    subject_1=fields.Integer(string="subject name")
    subject_2=fields.Integer(string="subject name")
    remarks=fields.Integer(string="remarks of subject",compute="_compute_total")

    @api.depends('subject_1', 'subject_2')
    def _compute_total(self):
        for order in self:
                total=order.subject_1 + order.subject_2
        order.remarks = total


