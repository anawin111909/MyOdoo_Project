from odoo import models, fields, api, _
from odoo.exceptions import ValidationError

class CoffeeIngredient(models.Model):
    _name = "coffee.shop.ingredient"
    _description = "Coffee Shop Ingredient"

    name = fields.Char(
        string="Ingredient Name",
        required=True
    )

    quantity = fields.Float(
        string="Quantity in Stock",
        digits=(10, 2),
        default=0.0
    )

    unit = fields.Selection(
        [
            ("kg", "Kilogram"),
            ("g", "Gram"),
            ("l", "Liter"),
            ("ml", "Milliliter"),
            ("pcs", "Pieces"),
        ],
        string="Unit of Measurement",
        default="pcs",
        required=True
    )

    minimum_quantity = fields.Float(
        string="Minimum quantity",
        default=0.0
    )

    cost_per_unit = fields.Float(
        string="Cost per Unit",
        digits=(10, 2),
        default=0.0
    )

    active = fields.Boolean(
        string="Active",
        default=True
    )

    @api.constrains('quantity', 'minimum_quantity', 'cost_per_unit')
    def _check_quantities(self):
        for record in self:
            if record.quantity < 0:
                raise ValidationError(
                    _("Current quantity cannot be negative.")
                )

            if record.minimum_quantity < 0:
                raise ValidationError(
                    _("Minimum quantity cannot be negative.")
                )
            if record.cost_per_unit < 0:
                raise ValidationError(
                    _("Cost per unit cannot be negative.")
                )
