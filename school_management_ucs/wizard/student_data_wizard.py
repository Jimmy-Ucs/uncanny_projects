from odoo import _, fields, models
from odoo.exceptions import UserError
import xlrd
import base64


class StudentDataWizard(models.TransientModel):
    _name = "student.data.wizard"
    _description = "Model is used to import student data"

    # imported_lines = fields.One2many('standard', 'invoice_line_update_id', string="Imported Lines")
    invoice_line_update_id = fields.Many2one("standard")


    excel_file = fields.Binary(string="Excel File", attachment=True)
    file_name = fields.Char('File Name')


    # def export_template_invoice(self):
    #     return self.env.ref("bi_import_invoice_line.action_export_template").report_action(self, config=False)

    def load_student_data(self):
        for record in self:
            if record.excel_file:
                workbook = xlrd.open_workbook(file_contents=base64.b64decode(record.excel_file))
                for sheet in workbook.sheets():
                    values = []
                    # missing_products = []
                    for row in range(1, sheet.nrows):
                        # if not sheet.cell(row, 0).value:
                        #     break
                        try:
                            name = sheet.cell(row, 2).value
                            code = sheet.cell(row, 1).value
                            desc = sheet.cell(row, 3).value
                            # record.invoice_line_update_id.name = name
                            # record.invoice_line_update_id.code = code
                            # record.invoice_line_update_id.desc = desc
                            # values.append(
                            #     (0,0,{
                            #         "code": code,
                            #         "name": name,
                            #         "desc": desc,
                            #     })
                            # )
                        except IndexError:
                            break
                    # print(">>>>>>>>>>>>>>>>>>>>>>>>>>",values)
                    # record.invoice_line_update_id = values
                    # record.invoice_line_update_id = False
                    # record.invoice_line_update_id = values
                    # record.invoice_line_update_id.missing_products_text = "\n\n\n".join(missing_products)
                        data = self.env['standard'].create({
                            'name': name,
                            'code': code,
                            'desc': desc,
                             })

                        values.append({
                        'name': name,
                        'code': code,
                        'desc': desc,
                    })

                    if values:
                        self.env['standard'].create(values)



        return {
            "effect": {
                "fadeout": "slow",
                "message": f"{len(values)} records successfully imported",
                "img_url": "/web/static/img/smile.svg",
                "type": "rainbow_man",
            }
        }
