from odoo import fields,models,_

class Standard(models.Model):
    _name="standard"
    _description = "academic month"
    _rec_name = "name"

    sequence=fields.Integer(string="Standard of student")
    name = fields.Char(string="Name")
    code = fields.Char(string="Student EN. no.")
    desc = fields.Text(string="Student Description")
    subject=fields.Char(string="Subject name")
    remarks=fields.Char(string="Remarks of Subject")

    # invoice_line_update_id = fields.Many2one("student.data.wizard")
    imported_lines = fields.One2many('student.data.wizard', 'invoice_line_update_id', string="Imported Lines")


    def action_import_student_data(self):
        return {
            "name": _("Import Student Data"),
            "type": "ir.actions.act_window",
            "view_mode": "form",
            "res_model": "student.data.wizard",
            "context": {"default_invoice_line_update_id": self.id},
            "target": "new",
        }