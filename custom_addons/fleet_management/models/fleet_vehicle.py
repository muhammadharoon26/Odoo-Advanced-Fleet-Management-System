# -*- coding: utf-8 -*-
from odoo import models, fields, api, _
from odoo.exceptions import ValidationError
from datetime import date

class FleetVehicle(models.Model):
    _name = 'fleet.management.vehicle'
    _description = 'Fleet Management Vehicle'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    # --- SQL CONSTRAINTS ---
    _sql_constraints = [
        ('license_plate_uniq', 'unique (license_plate)', 'License plate must be unique!'),
        ('vin_uniq', 'unique (vin)', 'VIN must be unique!'),
    ]

    # --- FIELDS ---
    name = fields.Char(
        string='Vehicle ID', required=True, copy=False, readonly=True,
        default=lambda self: _('New')
    )
    make = fields.Char(string='Make')
    model = fields.Char(string='Model')
    year = fields.Integer(string='Model Year')
    license_plate = fields.Char(string='License Plate', required=True)
    vin = fields.Char(string='VIN')
    active = fields.Boolean(default=True)
    driver_id = fields.Many2one('fleet.management.driver', string='Current Driver', tracking=True)
    driver_license = fields.Char(related='driver_id.license_number', string="Driver's License", readonly=True)
    state = fields.Selection([
        ('available', 'Available'),
        ('in_use', 'In Use'),
        ('maintenance', 'Maintenance'),
    ], string='Status', default='available', readonly=True, copy=False, tracking=True)
    vehicle_type = fields.Selection([
        ('car', 'Car'),
        ('van', 'Van'),
        ('truck', 'Truck'),
    ], string='Vehicle Type', default='car')
    notes = fields.Text(string='Notes')

    # --- PHASE 4 FIELDS ---
    image_1920 = fields.Image("Image")
    is_published = fields.Boolean(string="Publish on Website", copy=False)

    @api.constrains('year')
    def _check_year(self):
        for vehicle in self:
            if vehicle.year and vehicle.year > date.today().year + 1:
                raise ValidationError(_("Model year cannot be in the future!"))

    @api.onchange('vehicle_type')
    def _onchange_vehicle_type(self):
        if self.vehicle_type == 'truck':
            self.notes = "Heavy-duty vehicle. Check tire pressure weekly."
        else:
            self.notes = ""

    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            if vals.get('name', _('New')) == _('New'):
                vals['name'] = self.env['ir.sequence'].next_by_code('fleet.management.vehicle') or _('New')
        return super().create(vals_list)

    def action_set_in_use(self):
        self.write({'state': 'in_use'})

    def action_set_maintenance(self):
        self.write({'state': 'maintenance'})

    def action_set_available(self):
        self.write({'state': 'available'})