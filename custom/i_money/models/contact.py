from odoo import models, fields, api

class Contact(models.Model):
    _name = 'i.contact'
    _description = 'My Model'
    
    first_name = fields.Char(string="First Name", required=True)
    last_name = fields.Char(string="Last Name")
    phone = fields.Integer(string="Mobile Phone")
    email = fields.Char(string="Email", compute="_compute_mail", store=True)
    city = fields.Char(string="City")
    gender = fields.Selection([('male', 'Male'), ('female', 'Female')],string='Gender')
    birthdate = fields.Date(string="Birthdate")
    company_id = fields.Many2one('res.company', string="Company", default=lambda self: self.env.company)
    country_id = fields.Many2one('res.country', string="Country", related="company_id.country_id")
    state_id = fields.Many2one('res.country.state', string="State")
    number_lines = fields.One2many('i.contact.number', 'contact_id', string="Numbers")

    comment = fields.Text(string="Comment")
    note = fields.Html(string="Note")

    @api.depends('first_name', 'last_name')
    def _compute_mail(self):
        self.ensure_one()
        if self.first_name and self.last_name:
            self.email = "%s.%s@imoney.civ"%(self.first_name, self.last_name)
            return self.email