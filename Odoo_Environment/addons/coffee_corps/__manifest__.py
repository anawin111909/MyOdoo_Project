
{
    "name": "Coffee Corps Management",
    "version": "19.0.1.0",
    "category": "Services",
    "summary": "Coffee Shop Management System",
    "description": """
        Coffee Corps Management System

        Manage:
        - Coffee Products
        - Employees
        - Ingredients
        - Customer Orders
    """,
    "author": "Coffee Corps",
    "license": "LGPL-3",
    "depends": ["base"],
    
    "data": [
    "security/ir.model.access.csv",
    "views/product_view.xml",
    "views/employee_view.xml",
    "views/ingredient_view.xml",
    "views/order_view.xml",
    "views/recipe_view.xml",
    "views/menu_view.xml",
    ],
    "installable": True,
    "application": True,
}
