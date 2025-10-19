# -*- coding: utf-8 -*-
# from odoo import http


# class CustomSaleExtension(http.Controller):
#     @http.route('/custom_sale_extension/custom_sale_extension', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/custom_sale_extension/custom_sale_extension/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('custom_sale_extension.listing', {
#             'root': '/custom_sale_extension/custom_sale_extension',
#             'objects': http.request.env['custom_sale_extension.custom_sale_extension'].search([]),
#         })

#     @http.route('/custom_sale_extension/custom_sale_extension/objects/<model("custom_sale_extension.custom_sale_extension"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('custom_sale_extension.object', {
#             'object': obj
#         })

