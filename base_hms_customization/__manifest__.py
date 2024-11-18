# -*- coding: utf-8 -*-
{
    'name': "base_hms_customization , for deployment",

    "summary": "Apps basic Hospital Management system Healthcare Management Clinic Management apps manage clinic manage Patient hospital manage Healthcare system Patient Management Hospital Management Healthcare Management Clinic Management hospital Lab Test Request",

    'description': """
Long description of module's purpose
    """,

    'author': "My BEE DATA",
    'website': "https://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','basic_hms','point_of_sale'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'paper_format_customize/paperformat.xml',
        'views/menuitems.xml',
        'views/medical_inpatient_investigation_tree_view.xml',
        'views/medical_inpatient_investigation_form_view.xml',
        'views/investigation_information_views.xml',
        
        'report/investigation_reports.xml',
        'views/operation_notes_view.xml',
        'views/operation_notes_tree_view.xml',
        'report/operation_notes_reports.xml',
        'views/medical_patient_view.xml',
        
        'views/patient_room_form_view.xml',
        'views/patient_room_kanban_view.xml',
        'views/patient_room_tree_view.xml',
        
        'views/medical_inpatient_registeration_form_inherit.xml',
        'views/medical_patient_tree_view_inherit.xml',
        'views/product_category_form_view_inherit.xml',
        'views/medical_physicans_form_view_inherit.xml',
        'views/medical_physicans_tree_view_inherit.xml',
        
        'views/sale_order_line_from_view_inherit.xml',
        'views/account_move_line_views.xml',
        'views/referral_payment.xml',
        
        'views/res_config_settings_view.xml',
        
        
        # 'views/pos_order_line.xml',
       
        
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    
   
 
	


    
}

