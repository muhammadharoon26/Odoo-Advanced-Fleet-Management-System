# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request

class FleetWebsiteController(http.Controller):

    @http.route('/fleet', type='http', auth='public', website=True)
    def fleet_list(self, **kw):
        """
        Renders the main fleet page showing all published, available vehicles.
        """
        vehicles = request.env['fleet.management.vehicle'].search([
            ('is_published', '=', True),
            ('state', '=', 'available')
        ])
        return request.render('fleet_management.fleet_index_template', {
            'vehicles': vehicles
        })

    @http.route('/fleet/vehicle/<model("fleet.management.vehicle"):vehicle>', type='http', auth='public', website=True)
    def vehicle_details(self, vehicle):
        """
        Renders the detail page for a single vehicle.
        """
        return request.render('fleet_management.fleet_detail_template', {
            'vehicle': vehicle
        })

    @http.route('/fleet/inquiry', type='http', auth='public', website=True, methods=['POST'], csrf=True)
    def fleet_inquiry_submit(self, **post):
        """
        Handles the submission of the inquiry form.
        Creates a new inquiry record and shows a thank you page.
        """
        request.env['fleet.management.inquiry'].sudo().create({
            'vehicle_id': int(post.get('vehicle_id')),
            'customer_name': post.get('customer_name'),
            'customer_email': post.get('customer_email'),
            'customer_phone': post.get('customer_phone'),
            'message': post.get('message'),
        })
        return request.render('fleet_management.fleet_thank_you_template')