
from odoo import models, fields, api, _


class CoffeeOrder(models.Model):
    _name = "coffee.shop.order"
    _description = "Coffee Shop Order"
    _order = "order_date desc"

    name = fields.Char(
        string="Order Reference",
        required=True,
        copy=False,
        default=lambda self: _('New')
    )

    order_date = fields.Datetime(
        string="Order Date",
        default=fields.Datetime.now,
        required=True
    )

    employee_id = fields.Many2one(
        "coffee.shop.employee",
        string="Employee",
        required=True,
        ondelete="restrict"
    )

    # Connect Order with Order Lines
    order_line_ids = fields.One2many(
        "coffee.shop.order.line",
        "order_id",
        string="Order Lines"
    )

    total_amount = fields.Float(
        string="Total Amount",
        compute="_compute_total_amount",
        store=True
    )

    state = fields.Selection(
        [
            ("draft", "Draft"),
            ("confirmed", "Confirmed"),
            ("done", "Done"),
            ("cancelled", "Cancelled"),
        ],
        string="Status",
        default="draft",
        required=True
    )

    @api.depends("order_line_ids.subtotal")
    def _compute_total_amount(self):
        for order in self:
            order.total_amount = sum(
                order.order_line_ids.mapped("subtotal")
            )


class CoffeeOrderLine(models.Model):
    _name = "coffee.shop.order.line"
    _description = "Coffee Shop Order Line"

    order_id = fields.Many2one(
        "coffee.shop.order",
        string="Order",
        required=True,
        ondelete="cascade"
    )

    product_id = fields.Many2one(
        "coffee.shop.product",
        string="Product",
        required=True,
        ondelete="restrict"
    )

    quantity = fields.Integer(
        string="Quantity",
        default=1,
        required=True
    )

    price_unit = fields.Float(
        string="Unit Price",
        digits=(10, 2),
        required=True,
        default=0.0
    )

    subtotal = fields.Float(
        string="Subtotal",
        compute="_compute_subtotal",
        store=True
    )

    @api.onchange("product_id")
    def _onchange_product_id(self):
        if self.product_id:
            self.price_unit = self.product_id.price

    @api.depends("quantity", "price_unit")
    def _compute_subtotal(self):
        for line in self:
            line.subtotal = line.quantity * line.price_unit
