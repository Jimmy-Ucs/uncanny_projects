from odoo import models,api,fields,_

class MyWizard(models.TransientModel):
    _name = 'my.wizard'
    _description = 'My Wizard'

    name = fields.Char(string='Name')
    description = fields.Text('Description')

    def default_get(self, fields):
        res = super(MyWizard, self).default_get(fields)
        active_id = self._context.get('active_id')  # Get the selected record ID

        if active_id:
            record = self.env['my.model'].browse(active_id)
            res.update({
                'name': record.name,
                'description': record.description,
            })
        return res


    def action_save(self):
        pass
