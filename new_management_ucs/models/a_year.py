from odoo import fields,models,api,_
from odoo.exceptions import ValidationError

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
    sequence = fields.Char(string="roll-no")
    _sql_constraints = [('unique_sequence', 'UNIQUE(sequence)', 'roll-no must be unique!')]

    @api.constrains('s_date')
    def _check_joining_date(self):
        for rec in self:
            if rec.s_date > rec.st_date:
                raise ValidationError(("The start date of the academic year should be less than end date."))

    @api.constrains('c_year')
    def _check_unique_current_year(self):
        if self.c_year:
            active_years = self.search([('c_year', '=', True)])
            if active_years:
                raise ValidationError("Error! You cannot set two current years active!")
