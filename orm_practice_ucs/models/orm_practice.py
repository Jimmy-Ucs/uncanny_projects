from odoo import api,fields,models,_

class OrmPractice(models.Model):

    _name = "orm.practice"
    _description = " orm practice"

    name=fields.Char(string="name")
    surname=fields.Char(string="surname")
    age=fields.Integer(string="age: ")
    is_boolean = fields.Boolean()
    state = fields.Selection([('confirmed','Confirmed'),('cancelled', 'Cancelled'),], string='State')
    appointments = fields.Integer(string="total appointment:")
    def create(self, vals):
        print(vals)
        rtn=super(OrmPractice,self).create(vals)
        print(rtn)
        return rtn

    def write(self,vals):
        print(vals)
        rtn=super(OrmPractice,self).write(vals)
        print(rtn)

    def custom_method(self):
    #     print("activated")
    #
    #     # self.name="unknown"
    #     # self.age=0
    #     # self.surname="unknown"
        self.update({'name':'unknown','surname':'unknown','age':0})
    #     self.is_boolean = True

        # records=self.name
        # records.write({'name':'unknown'})

    def action_confirm(self):
        self.write({'state': 'confirmed'})

    def action_cancel(self):
        self.write({'state':'cancelled'})

    def show_appointments(self):
        # for res in self:
            total_len = len(self.env['orm.practice'].search([('name', '=', 'jimmy')]))
            appointments=total_len
            # res.appointments = total_len
            return {

            'name': 'Orm Practice',
            'view_mode': 'list,form',
            'res_model': 'orm.practice',
            'type': 'ir.actions.act_window',
        }