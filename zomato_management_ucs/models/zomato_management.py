from odoo import api,fields,models,_
class ZomatoManagement(models.Model):
    _name = "zomato.management"
    _description = "Zomato Management"
    _rec_name = "delivery_person"
    _order="delivery_person"

    delivery_person = fields.Char(string="Name")
    employee_code = fields.Integer(string="employee code")
    order = fields.Char(string="Total order of day:")
    t_date = fields.Datetime(string="enter the date:")
    p_image=fields.Image(string="")
    show_hr_icon_display=fields.Image(string="")
    image_128=fields.Image(string="")
    avatar_128=fields.Image(string="")
    hr_icon_display=fields.Image(string="")
    partner_id = fields.Many2one("res.partner", string="Customer")
    partner_ids = fields.Many2many("res.partner", string="Customers")
    # order_id = fields.One2many("pg.management","zomato_id")