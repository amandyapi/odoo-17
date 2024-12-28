from odoo import models, fields, api
from odoo.exceptions import ValidationError
 
import logging
 
_logger = logging.getLogger(__name__)
 
class Partner(models.Model):
    _inherit = "res.partner"
 
    sequence = fields.Char(string='Sequence', readonly=True, default=lambda self: self.env['ir.sequence'].next_by_code('res_partner_sequence'))
 
    @api.constrains('name')
    def _check_name(self):
        for rec in self:
            partner = self.env['res.partner'].search([('name', '=', rec.name), ('company_id', '=', self.env.company_id.id)], limit=1)
            _logger.info("================================================> %s <=================================================", partner.name)
            if partner:
                raise ValidationError("This partner already exist")
            else:
                pass