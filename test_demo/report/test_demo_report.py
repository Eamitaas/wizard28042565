
# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from datetime import datetime, timedelta
from odoo.tools import DEFAULT_SERVER_DATE_FORMAT, DEFAULT_SERVER_DATETIME_FORMAT
from odoo import api, fields, models, _
from odoo.exceptions import AccessError, UserError, ValidationError
import math

# 4
class test_demo_report_id(models.AbstractModel):
    _name = 'report.test_demo.test_demo_report_id'

    @api.model
    def _get_report_values(self, docids, data=None):
        print('_get_report_values')
        print('data ',data)
        print('active_model ', self.env.context.get('active_model'))
        if not data.get('form') or not self.env.context.get('active_model'):
            raise UserError(_("Form content is missing, this report cannot be printed."))

        model = self.env.context.get('active_model')
        docs = self.env[model].browse(self.env.context.get('active_ids', []))

        domain = [('date', '>=', docs.date_from),
                  ('date', '<=', docs.date_to)]
        test_demo_ids = self.env['test.demo'].search(domain)
        print('test_demo_ids ',test_demo_ids)

        docargs = {
            'doc_ids': docids,
            'data': data['form'],
            'docs': docs,
            'test_demo_ids': test_demo_ids,
        }
        return docargs
