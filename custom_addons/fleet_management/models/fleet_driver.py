# -*- coding: utf-8 -*-
from odoo import models, fields, api

class FleetDriver(models.Model):
    _name = 'fleet.management.driver'
    _description = 'Fleet Management Driver'

    name = fields.Char(string='Driver Name', required=True)
    license_number = fields.Char(string='Driver License Number', required=True)
    contact_phone = fields.Char(string='Contact Phone')
    contact_email = fields.Char(string='Contact Email')
    active = fields.Boolean(default=True)
    
    # --- PHASE 2 FIELDS ---
    vehicle_ids = fields.One2many('fleet.management.vehicle', 'driver_id', string='Assigned Vehicles')
    vehicle_count = fields.Integer(string='Vehicle Count', compute='_compute_vehicle_count')
    
    @api.depends('vehicle_ids')
    def _compute_vehicle_count(self):
        for driver in self:
            driver.vehicle_count = len(driver.vehicle_ids)