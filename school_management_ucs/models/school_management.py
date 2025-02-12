from odoo import fields,models,_, api

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
    age = fields.Integer(string="student age")
    height = fields.Float(string="student height")
    weight = fields.Float(string="student weight")
    subject=fields.Char(string="subject name")
    remarks=fields.Char(string="remarks of subject")
    p_image=fields.Image(string="image of student")


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    invoice_id = fields.Many2one("account.move", string="Invoice")


    # def test_method(self):
    #     for record in self:
    #         PurchaseObj = self.env['purchase.order']
    #         self.env['purchase.order'].create({'invoice_id':record.invoice_id})
            # self.env['purchase.order'].write({'invoice_id':record.invoice_id})
            # self.env['purchase.order'].update({'invoice_id':record.invoice_id})
            # purchase_id = self.env['purchase.order'].search([('name', '=', 'PO0001'),('partner_id', '=', record.partner_id.id)], limit=1)
            # # int id
            # purchase_browse_id = self.env['purchase.order'].browse(purchase_id) #return Record set
            # # purchase.order(20)
            #
            # purchase_filtered_id = self.env['purchase.order'].filtered(lambda x: x.name)
            # print("+++++++++++", purchase_id)
        # return  PurchaseObj


    x_custom_field = fields.Char(string='Custom Field')

    @api.model
    def create_sale_order(self, partner_id, product_ids, quantities, price_units, custom_field_value):

            order = self.create({
                'partner_id': partner_id,
                'date_order': fields.Datetime.now(),
                'x_custom_field': custom_field_value,
                'order_line': [(0, 0, {
                    'product_id': product_id,
                    'product_uom_qty': qty,
                    'price_unit': price,
                }) for product_id, qty, price in zip(product_ids, quantities, price_units)],
            })
            return order
    # def write(self,vals_list):
    #     res = super(SaleOrder, self).write(vals_list)
    #     return res True Or False
    #
    # def unlink(self):
    #     res = super(SaleOrder, self).unlink()
    #     return res True or False
    #
    # def copy(self):
    #     res = super(SaleOrder, self).copy()
    #     return res record





class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'
    #
    # sequence = fields.Integer(string="Sequence", default=10)
    invoice_id = fields.Many2one("account.move", string="Invoice")

