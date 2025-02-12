from odoo import api, fields, models, _


class PgManagement(models.Model):
    _name = "pg.management"
    _description = "PG management"

    name = fields.Char(string="Name")
    surname = fields.Char(string="surname")
    address = fields.Text(string="address")
    # zomato_id = fields.Many2one("zomato.management")