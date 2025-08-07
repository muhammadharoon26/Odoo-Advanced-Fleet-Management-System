# -*- coding: utf-8 -*-
from odoo import models, fields, api

class FleetDriver(models.Model):
    _name = 'fleet.management.driver'
    _description = 'Fleet Management Driver'

    # --- SQL CONSTRAINTS ---
    _sql_constraints = [
        ('license_number_uniq', 'unique (license_number)', 'Driver License number must be unique!'),
    ]

    name = fields.Char(string='Driver Name', required=True)
    license_number = fields.Char(string='Driver License Number', required=True)
    contact_phone = fields.Char(string='Contact Phone')
    contact_email = fields.Char(string='Contact Email')
    active = fields.Boolean(default=True)
    vehicle_ids = fields.One2many('fleet.management.vehicle', 'driver_id', string='Assigned Vehicles')
    vehicle_count = fields.Integer(string='Vehicle Count', compute='_compute_vehicle_count')

    @api.depends('vehicle_ids')
    def _compute_vehicle_count(self):
        for driver in self:
            driver.vehicle_count = len(driver.vehicle_ids)

    # --- PHASE 3: SMART BUTTON METHOD ---
    def action_view_vehicles(self):
        return {
            'name': 'Assigned Vehicles',
            'type': 'ir.actions.act_window',
            'res_model': 'fleet.management.vehicle',
            'view_mode': 'list,form',
            'domain': [('id', 'in', self.vehicle_ids.ids)],
            'target': 'current',
        }