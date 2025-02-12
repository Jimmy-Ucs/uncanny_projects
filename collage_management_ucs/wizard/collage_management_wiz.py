from odoo import api,fields,models,_

class MyWizard(models.TransientModel):
    _name = "my.wizard"
    student_id = fields.Integer(string="student-id")
    contact = fields.Char(string="contact number")
    description = fields.Text(string="describe")


    def confirm(self):
        print("successfully confirmed")


    def cancel(self):
        print("successfully confirmed")




