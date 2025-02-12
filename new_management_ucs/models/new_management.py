from odoo import fields,models,_, api
from datetime import timedelta
from dateutil.relativedelta import relativedelta
from odoo.exceptions import ValidationError


class SchoolManagement(models.Model):

    _name = "school.management"
    _description = "school management"
    _rec_name = "state"



    mobile = fields.Integer(string="mobile no")
    contact = fields.Integer(string="contact no")
    zip = fields.Integer(string="pin code")
    country = fields.Many2one("res.country", string="country name")
    state = fields.Many2one("res.country.state",string="state name")
    date = fields.Date(string="admission date")
    l_date = fields.Date(string="leave date")
    gender = fields.Selection([('1.', 'Male'), ('2.', 'Female'),('3','Others')], string='select gender')
    height = fields.Float(string="student height")
    weight = fields.Float(string="student weight")
    subject=fields.Char(string="subject name")
    remarks=fields.Char(string="remarks of subject")
    p_image=fields.Image(string="image of student")
    state_s = fields.Selection([('draft','Draft'),('done','Done'),('terminate','Terminate'),('cancel', 'Cancel'),], string='State')
    birth_date = fields.Date(string="birth Date",required=True)
    age = fields.Integer(string="student age" , compute="_compute_age")
    s_code = fields.Char(string="student-code")

    @api.model
    def create(self,vals):
        vals['s_code']=self.env['ir.sequence'].next_by_code("school.management")
        return super(SchoolManagement,self).create(vals)

    @api.depends('birth_date')
    def _compute_age(self):
        for record in self:
            record.age = 0

            if record.birth_date :
                record.age = relativedelta(fields.Date.from_string(fields.Date.today()),
                    fields.Date.from_string(record.birth_date)).years
    #         elif record.birth_date==fields.date.today():

    def action_draft(self):
        self.write({'state_s': 'draft'})

    def action_done(self):
        self.write({'state_s':'done'})

    def action_terminate(self):
        self.write({'state_s': 'terminate'})

    def action_cancel(self):
        self.write({'state_s':'cancel'})

    @api.constrains('date')
    def _check_joining_date(self):
        for rec in self:
            if rec.date > rec.l_date:
                raise ValidationError(("The joining date must be greater than today's date."))