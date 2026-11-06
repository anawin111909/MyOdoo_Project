
from odoo import models, fields


class CoffeeEmployee(models.Model):
    _name = "coffee.shop.employee"
    _description = "Coffee Shop Employee"

    name = fields.Char(
        string="Employee Name",
        required=True
    )

    role = fields.Selection(
        [
            ("manager", "Manager"),
            ("barista", "Barista"),
            ("cashier", "Cashier"),
        ],
        string="Position",
        default="barista",
        required=True
    )

    phone = fields.Char(
        string="Phone Number"
    )

    email = fields.Char(
        string="Email"
    )

    hire_date = fields.Date(
        string="Hire Date"
    )

    salary = fields.Float(
        string="Monthly Salary",
        digits=(10, 2),
        default=0.0
    )

    active = fields.Boolean(
        string="Active",
        default=True
    )
