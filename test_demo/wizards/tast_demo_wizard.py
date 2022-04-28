
from odoo import api, fields, models, SUPERUSER_ID, _
from odoo.exceptions import AccessError, UserError, ValidationError
from datetime import datetime

# 1
class TastDemoWizard(models.TransientModel):
    _name = 'test.demo.wizard'

    date_from = fields.Date('Date From')
    date_to = fields.Date('Date to')
    #fields.Date ฟิวปุ่ม

    def print_pdf_report(self):
        [data] = self.read()
        datas = {'form': data}

        return self.env.ref('test_demo.test_demo_report').report_action(self, data=datas, config=False)