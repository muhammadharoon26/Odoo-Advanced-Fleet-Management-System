# -*- coding: utf-8 -*-
from odoo import models, fields, api

class FleetVehicle(models.Model):
    _name = 'fleet.management.vehicle'
    _description = 'Fleet Management Vehicle'

    name = fields.Char(string='Vehicle Name', required=True, help="A user-friendly name for the vehicle (e.g., 'Sales Car 1')")
    make = fields.Char(string='Make', help="Manufacturer of the vehicle (e.g., 'Toyota')")
    model = fields.Char(string='Model', help="Model of the vehicle (e.g., 'Camry')")
    year = fields.Integer(string='Year')
    license_plate = fields.Char(string='License Plate', required=True)
    vin = fields.Char(string='VIN')
    active = fields.Boolean(default=True, help="Set to false to hide the vehicle without removing it.")

    # --- PHASE 2 FIELDS ---
    driver_id = fields.Many2one('fleet.management.driver', string='Current Driver')
    driver_license = fields.Char(related='driver_id.license_number', string="Driver's License", readonly=True)

    state = fields.Selection([
        ('available', 'Available'),
        ('in_use', 'In Use'),
        ('maintenance', 'Maintenance'),
    ], string='Status', default='available', readonly=True, copy=False)

    # --- PHASE 2 BUTTON METHODS ---
    def action_set_in_use(self):
        self.write({'state': 'in_use'})

    def action_set_maintenance(self):
        self.write({'state': 'maintenance'})

    def action_set_available(self):
        self.write({'state': 'available'})