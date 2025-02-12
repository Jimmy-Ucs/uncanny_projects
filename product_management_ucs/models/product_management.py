from odoo import api,models,fields,_
from datetime import timedelta
from dateutil.relativedelta import relativedelta

class ProductManagement(models.Model):

    _name = "product.management"
    _description = "product management"


    my_date = fields.Date(string="Original Date")
    years_to_add = fields.Integer(string="Years to Add")
    exp_date = fields.Date(string="New Date", compute="_compute_new_date")
    @api.depends('my_date','years_to_add')
    def _compute_new_date(self):
        for record in self:
            if record.my_date and record.years_to_add:
                record.exp_date = record.my_date + relativedelta(years=record.years_to_add)
            return record.exp_date
