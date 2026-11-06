from odoo import models, fields


class CoffeeProduct(models.Model):
    _name = "coffee.shop.product"
    _description = "Coffee Shop Product"

    name = fields.Char(
        string="Product Name",
        required=True
    )

    category = fields.Selection(
        [
            ("coffee", "Coffee"),
            ("tea", "Tea"),
            ("non_coffee", "Non-Coffee"),
            ("dessert", "Dessert"),
        ],
        string="Category",
        default="coffee"
    )

    price = fields.Float(
        string="Price",
        digits=(10, 2),
        required=True,
        default=0.0
    )

    description = fields.Text(
        string="Description"
    )

    active = fields.Boolean(
        string="Active",
        default=True
    )
