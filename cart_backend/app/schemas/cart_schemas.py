"""
Marshmallow schemas for cart operations with OpenAPI support.

These schemas define validation rules and documentation for the cart API.
"""

from marshmallow import Schema, fields, validate


class CartItemSchema(Schema):
    product_id = fields.Str(
        required=True,
        description="Unique product identifier",
        validate=validate.Length(min=1),
        example="SKU-12345",
    )
    quantity = fields.Int(
        required=True,
        description="Quantity to add",
        validate=validate.Range(min=1),
        example=2,
    )


class CartItemResponseSchema(Schema):
    product_id = fields.Str(required=True, description="Unique product identifier")
    quantity = fields.Int(required=True, description="Quantity in the cart")


class CartResponseSchema(Schema):
    cart_id = fields.Str(required=True, description="Cart identifier (user/session)")
    items = fields.List(fields.Nested(CartItemResponseSchema), required=True)
    total_items = fields.Int(required=True, description="Total quantity across items")


class DeleteItemSchema(Schema):
    product_id = fields.Str(
        required=True,
        description="Unique product identifier to remove",
        validate=validate.Length(min=1),
        example="SKU-12345",
    )
