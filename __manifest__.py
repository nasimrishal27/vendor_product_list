# -*- coding: utf-8 -*-
{
    'name': "Vendor Product List",
    'version': '1.0',
    'depends': ['purchase'],
    'sequence': 1,
    'author': "Suni",
    'category': 'All',
    'description': """
    Property Management
    """,
    # data files always loaded at installation
    'data': [
        'views/purchase_order.xml',
        'views/vendor_product_list_menu_view.xml',
    ],
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
}

