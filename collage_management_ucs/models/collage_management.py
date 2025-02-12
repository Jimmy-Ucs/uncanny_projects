from odoo import api,fields,models,_

class CollageManagement(models.Model):
    _name="collage.management"
    _description = "collage management"
    _order="name"

    name=fields.Many2one("res.partner",string="customer name")
    contact=fields.Char(string="contact number")
    address=fields.Text(string="home address")
    p_image=fields.Image()
    student_id = fields.Integer(string="student-id")
    description = fields.Text(string="describe")

    @api.onchange('name')
    def _onchange_partner_id(self):
        self.contact= self.name.customer_id

    @api.model
    def default_get(self, fields):
        res = super("my.wizard", self).default_get(fields)
        active_ids = self._context.get('active_id')  # Get the selected record ID

        if active_ids:
            record = self.env['collage.management'].browse(self._context.get("active_ids"))
            res.update({
                'name': record.name,
                'description': record.description,
            })
        return res

    def action_confirm(self):
        return self.env['ir.actions.act_window']._for_xml_id("collage_management_ucs.action_open_my_wizard")
        # return {'type': 'ir.actions.act_window',
        #         'res_model' : 'my.wizard',
        #         'view_mode':'form',
        #         'target':'new'}


class ResPartner(models.Model):
    _inherit = "res.partner"
    customer_id=fields.Char(string="customer_id")


