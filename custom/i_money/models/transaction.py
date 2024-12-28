from odoo import models, fields, api

class Transaction(models.Model):
    _name = 'i.transaction'
    _description = 'Imoney Transaction'
    
    operator = fields.Selection([('wave', 'Wave'),('orange', 'Orange'), ('mtn', 'MTN'), ('moov', 'MOOV')],string='Operator'), required=True
    amount = fields.Int(string="Amount", required=True)
    operationType = fields.Int(string="operation Type", required=True)
    mobile = fields.Char(string="Mobile Phone", required=True)
    countryCode = fields.Selection([('CI', 'CI'),('SN', 'SN')],string='Country Code', required=True)
    otp = fields.Char(string="OTP")
    clientReference = fields.Char(string="Client Reference")

    description = fields.Text(string="Description")