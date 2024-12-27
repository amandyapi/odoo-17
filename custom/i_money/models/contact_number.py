from odoo import models, fields
 
class ContactNumber(models.Model):
    _name = 'i.contact.number'
    _description = 'other contact number'
 
    contact_id = fields.Many2one('i.contact',string='Contact')
    phone = fields.Char(string='Phone')
    state = fields.Boolean(string='Status')
 