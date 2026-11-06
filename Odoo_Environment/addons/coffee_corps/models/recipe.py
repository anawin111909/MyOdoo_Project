from odoo import models, fields, api, _
from odoo.exceptions import ValidationError


class CoffeeRecipeLine(models.Model):
    _name = "coffee.shop.recipe.line"
    _description = "Coffee Product Recipe"

    product_id = fields.Many2one(
        "coffee.shop.product",
        string="Product",
        required=True,
        ondelete="cascade"
    )

    ingredient_id = fields.Many2one(
        "coffee.shop.ingredient",
        string="Ingredient",
        required=True,
        ondelete="restrict"
    )

    quantity = fields.Float(
        string="Quantity Required",
        required=True,
        default=0.0
    )

    @api.constrains("quantity")
    def _check_quantity(self):
        for recipe in self:
            if recipe.quantity <= 0:
                raise ValidationError(
                    _("Ingredient quantity must be greater than zero.")
                )