# -*- coding: utf-8 -*-
{
    'name': "product_price2",

    'summary': """
        Agrega un nuevo campo para precio en el form del producto
        """,

    'description': """
        Agrega un nuevo campo para precio en el form del producto
    """,

    'author': "Javito",
    'website': "http://www.ymant.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Sale',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['product'],

    # always loaded
    'data': [
        "views/product_view.xml",
    ],
}
