# -*- coding: utf-8 -*-
from odoo import http

# class Addonsstock(http.Controller):
#     @http.route('/addonsstock/addonsstock/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/addonsstock/addonsstock/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('addonsstock.listing', {
#             'root': '/addonsstock/addonsstock',
#             'objects': http.request.env['addonsstock.addonsstock'].search([]),
#         })

#     @http.route('/addonsstock/addonsstock/objects/<model("addonsstock.addonsstock"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('addonsstock.object', {
#             'object': obj
#         })