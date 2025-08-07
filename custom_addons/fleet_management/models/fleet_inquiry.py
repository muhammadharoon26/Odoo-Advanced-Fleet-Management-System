# -*- coding: utf-8 -*-
from odoo import models, fields

class FleetInquiry(models.Model):
    _name = 'fleet.management.inquiry'
    _description = 'Fleet Website Inquiry'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    vehicle_id = fields.Many2one('fleet.management.vehicle', string='Vehicle', required=True)
    customer_name = fields.Char(string='Your Name', required=True, tracking=True)
    customer_email = fields.Char(string='Your Email', required=True, tracking=True)
    customer_phone = fields.Char(string='Your Phone')
    message = fields.Text(string='Message', required=True)