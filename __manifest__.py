# -*- coding: utf-8 -*-
{
    'name': "Orisdi Barcode",

    'summary': """Barcoder Customization""",

    'author': "Integerated Path",
    'website': "https://www.int-path.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Inventory',
    'version': '1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'stock_barcode'],

    # always loaded
    'data': [
        'reports/saleorder_barcode_report.xml',
    ],
}
