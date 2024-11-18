# -*- coding: utf-8 -*-
# from odoo import http


# class BaseHmsCustomization(http.Controller):
#     @http.route('/base_hms_customization/base_hms_customization', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/base_hms_customization/base_hms_customization/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('base_hms_customization.listing', {
#             'root': '/base_hms_customization/base_hms_customization',
#             'objects': http.request.env['base_hms_customization.base_hms_customization'].search([]),
#         })

#     @http.route('/base_hms_customization/base_hms_customization/objects/<model("base_hms_customization.base_hms_customization"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('base_hms_customization.object', {
#             'object': obj
#         })

