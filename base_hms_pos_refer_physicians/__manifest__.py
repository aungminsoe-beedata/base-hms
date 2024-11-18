# -*- coding: utf-8 -*-

{
    'name': 'Employee Real Refer Sale Order, for deployment',
    'Version': '17.0.1.0.0',
    'category': 'Extra Tools',
    'summary': 'This module is used to set refer persons on pos order line',
    'description': 'This module allows you to assign refer physicians to order'
                   'lines in the Point of Sale (POS)',
    'author': 'Aung Min Soe',
    'company': 'Bee Data Myanmar',
    'maintainer': 'Bee Data Myanmar Software  Solutions',
    'website': "https://www.beedatamyanmar.com",
    'depends': ['point_of_sale','base_hms_customization','basic_hms'],
    'data': [
        'views/pos_orderline_views.xml',
    ],
    'assets': {
        'point_of_sale._assets_pos': [
                'base_hms_pos_refer_physicians/static/src/js/pos_load_data.js',
                'base_hms_pos_refer_physicians/static/src/js/pos_screen.js',
                
                'base_hms_pos_refer_physicians/static/src/js/pos_orderline.js',
                'base_hms_pos_refer_physicians/static/src/xml/pos_screen_templates.xml',
                'base_hms_pos_refer_physicians/static/src/xml/orderline_templates.xml',
            ],
    },
    'images': ['static/description/banner.jpg'],
    'license': 'AGPL-3',
    'installable': True,
    'auto_install': False,
    'application': False,
}
