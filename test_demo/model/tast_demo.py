from odoo import api, fields, models, SUPERUSER_ID, _
from odoo.exceptions import AccessError, UserError, ValidationError
from datetime import datetime


#จะทำ sale ใหม่ต้องใส่ security

class Tast(models.Model):
    _name = "test.demo"
    _inherit = ['portal.mixin', 'mail.thread', 'mail.activity.mixin', 'utm.mixin']
    _description = "Tast"

    # name = fields.Many2one('res.partner', string='Partner')
    # part_line = fields.One2many('pas.satisfaction.line', 'part_id', string='tast')
    name = fields.Many2one('res.partner', string='ลูกค้า')
    address = fields.Char('ที่อยู่')
    # address1 = fields.Char('ที่อยู่')
    address_1 = fields.Char('ที่อยู่')
    # number = fields.Float('เลขประจำตัวผู้เสียภาษี')
    number = fields.Char('เลขประจำตัวผู้เสียภาษี')
    nameadd = fields.Char('ผู้ติดต่อ')
    numberorder = fields.Char('เลขที่ใบส่งของชั่วคราว')
    date = fields.Date(string='วันที่', default=datetime.today())
    usesale = fields.Char('พนักงานขาย')
    payment = fields.Char('เงือนไขการชำระเงิน')
    dateline = fields.Date(string='กำหนดยื่นราคาถึงวันที่่', default=datetime.today())
    datetime_line = fields.Datetime(string='กำหนดยื่นราคาถึงวันที่่', default=lambda self: fields.Datetime.now())
    numberrefer = fields.Char('เลขอ้างอิง')
    sum = fields.Float('รวม' , compute='_compute_amount',digits='Product Price')
    discount_id = fields.Char('ส่วนลด')
    remaining = fields.Float('คงเหลือ',digits='Product Price')
    tax = fields.Float('ภาษีมูลค่าเพิ่ม 7%',digits='Product Price')
    amount = fields.Float('ยอดเงินสุทธิ', compute='_compute_amount',digits='Product Price')
    pricth = fields.Char('บาทไทย')
    part_line = fields.One2many('part.line', 'part_id', string='สินค้า')

    @api.depends('part_line.price')
    def _compute_amount(self):
        for obj in self: #วนลูปรอบแรก วนลูปเซลล์
            sum = 0.0
            for line in obj.part_line: #วนลูปรอบสอง วนลูปไลน์
                print('line ', line)
                sum += line.price
            print('sum', sum)
            obj.tax = sum * 0.07 # ค่า Vat
            obj.sum = sum # ค่ารวมของเซลล์
            obj.amount = sum + sum * 0.07 # รวมกับค่า vat แล้ว
            obj.remaining = sum

    @api.onchange('name')
    def onchange_name(self):
        self.address = self.name.street
        self.address_1 = self.name.city
        # self.address_1 = self.name.payment_term_id.id


class PartLine(models.Model):
    _name = "part.line"

    part_id = fields.Many2one('test.demo', string='test ref')
    details = fields.Many2one('product.template', string='รายละเอียดสินค้า')
    quantity = fields.Float('จำนวน')
    unit = fields.Char('หน่วย')
    priceunit = fields.Float('ราคาหน่วยละ')
    discount = fields.Char('ส่วนลด')
    price = fields.Float('จำนวนเงิน',compute='_compute_price_total')


    @api.depends('quantity', 'priceunit')
    def _compute_price_total(self):
        for obj in self:
            obj.price = obj.quantity * obj.priceunit

    @api.onchange('details')
    def onchange_details(self):
        self.priceunit = self.details.list_price
