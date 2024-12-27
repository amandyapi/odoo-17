{
    'name': 'E-money',
    'version': '1.1',
    'category': 'Tools',
    'summary': 'A simple Odoo module example',
    'description': """
        This module demonstrates how to create a new model and menu item in Odoo.
    """,
    'author': 'TKR',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/contact_views.xml',
        'views/menu_views.xml'
    ],
    'installable': True,
    'application': True,
}