{
    'name': 'E-money',
    'version': '1.1',
    'category': 'Tools',
    'summary': 'A simple Odoo module example',
    'description': """
        This module demonstrates how to create a new model and menu item in Odoo.
    """,
    'author': 'TKR',
    'depends': ['base', 'web', 'contacts'],
    'data': [
        'security/ir.model.access.csv',
        'security/i_money_group.xml',
        'security/i_money_rule.xml',
        'data/contact_data.xml',
        'data/contact_sequence.xml',
        'report/contact_report_template.xml',
        'report/action_contact_report.xml',
        'views/contact_views.xml',
        'views/partner_view.xml',
        'views/menu_views.xml'
    ],
    'installable': True,
    'application': True,
}