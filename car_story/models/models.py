from odoo import models, fields, api

class CarStory(models.Model):
    _name = 'car.story'
    _description = 'Car Story Form'

    owner_name = fields.Char(string="Owner Name", required=True)
    color = fields.Selection([
        ('red', 'Red'),
        ('blue', 'Blue'),
        ('green', 'Green'),
        ('black', 'Black'),
        ('white', 'White'),
        ('silver', 'Silver'),
    ], string='Color')
    make = fields.Selection([
        ('hyundai', 'Hyundai'),
        ('kia', 'Kia'),
    ], string='Make', required=True, default='hyundai')
    model = fields.Char(string='Model', required=False)
    vin = fields.Char(string="VIN")
    mileage = fields.Float(string="Mileage")
    year = fields.Selection([(str(x), str(x)) for x in range(1990, 2026)], string='Year', required=True)
    reached_company = fields.Boolean(string="Have you reached the company?")
    out_of_pocket = fields.Selection([
        ('not_pay', 'Not Paid'),
        ('100_500', '100-500'),
        ('500_1000', '500-1000'),
        ('1000_2000', '1000-2000'),
        ('more_2000', 'More than 2000'),
    ], string="How much have you paid to fix it?")
    story = fields.Text(string="Tell your story and describe the quality issue")
    image_ids = fields.Many2many('ir.attachment', string='Images')

