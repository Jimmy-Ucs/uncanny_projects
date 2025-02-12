from odoo import models, fields, api

# Main model definition
class MyModel(models.Model):
    _name = 'my.model'
    _description = 'My Model'

    name = fields.Char('Name')
    description = fields.Text('Description')



    def action_confirm(self):
        # return self.env['ir.actions.act_window']._for_xml_id("wizard_management_ucs.action_open_my_wizard")

        return {'type': 'ir.actions.act_window',
                 'res_model' : 'my.wizard',
                 'view_mode':'form',
                 'target':'new',
                'context': {
                    'default_name':self.name,
                    'default_description': self.description}
                }

