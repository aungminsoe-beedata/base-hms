# -*- coding: utf-8 -*-
# from odoo import http


# class Uploadimagewebcam(http.Controller):
#     @http.route('/uploadimagewebcam/uploadimagewebcam', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/uploadimagewebcam/uploadimagewebcam/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('uploadimagewebcam.listing', {
#             'root': '/uploadimagewebcam/uploadimagewebcam',
#             'objects': http.request.env['uploadimagewebcam.uploadimagewebcam'].search([]),
#         })

#     @http.route('/uploadimagewebcam/uploadimagewebcam/objects/<model("uploadimagewebcam.uploadimagewebcam"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('uploadimagewebcam.object', {
#             'object': obj
#         })

