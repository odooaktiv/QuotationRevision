# -*- coding: utf-8 -*-
{
    'name': "Quotation Revision",

    'summary': """
        Quotation Revised History""",

    'description': """
        We can manage Quotation Revised History in sale order.
    """,

    'author': "Aktiv software ",
    'website': "http://www.aktivsoftware.com/",

    # Categories can be used to filter modules in modules listing
    'category': 'Sales',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['sale_management'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/sale_order_views.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
    ],

    'images': ['static/description/banner.jpg'],
    'application': True,
}
