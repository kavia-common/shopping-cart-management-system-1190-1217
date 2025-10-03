"""
Cart API routes.

Provides RESTful endpoints to:
- View a cart
- Add an item
- Delete an item

All endpoints are documented via flask-smorest and Marshmallow schemas.
"""

from flask_smorest import Blueprint
from flask.views import MethodView

from app.schemas.cart_schemas import (
    CartItemSchema,
    DeleteItemSchema,
    CartResponseSchema,
)
from app.services.cart_service import CartService

blp = Blueprint(
    "Cart",
    "cart",
    url_prefix="/cart",
    description="Shopping cart operations (Ocean Professional theme)",
)

_service = CartService()


@blp.route("/<string:cart_id>", methods=["GET"])
class CartResource(MethodView):
    # PUBLIC_INTERFACE
    def get(self, cart_id: str):
        """
        Get the current state of a cart.
        Returns the cart with items and totals.
        """
        """
        ---
        get:
          summary: View cart
          description: Retrieve the current contents and totals of a given cart.
          parameters:
            - in: path
              name: cart_id
              required: true
              description: Cart identifier (user or session id)
              schema:
                type: string
          responses:
            200:
              description: Cart retrieved successfully
              content:
                application/json:
                  schema: CartResponseSchema
        """
        cart = _service.view_cart(cart_id)
        return cart, 200


@blp.route("/<string:cart_id>/items", methods=["POST", "DELETE"])
class CartItemsResource(MethodView):
    # PUBLIC_INTERFACE
    @blp.arguments(CartItemSchema, location="json")
    @blp.response(200, CartResponseSchema)
    def post(self, data, cart_id: str):
        """
        Add item to cart.

        Body:
        - product_id: string
        - quantity: integer >= 1
        Returns updated cart.
        """
        """
        ---
        post:
          summary: Add item to cart
          description: Add a product with a specified quantity to the cart.
          parameters:
            - in: path
              name: cart_id
              required: true
              description: Cart identifier (user or session id)
              schema:
                type: string
          requestBody:
            required: true
            content:
              application/json:
                schema: CartItemSchema
          responses:
            200:
              description: Item added, updated cart returned
              content:
                application/json:
                  schema: CartResponseSchema
        """
        product_id = data["product_id"]
        quantity = int(data["quantity"])
        cart = _service.add_item(cart_id, product_id, quantity)
        return cart

    # PUBLIC_INTERFACE
    @blp.arguments(DeleteItemSchema, location="json")
    @blp.response(200, CartResponseSchema)
    def delete(self, data, cart_id: str):
        """
        Delete item from cart.

        Body:
        - product_id: string
        Returns updated cart (no-op if item absent).
        """
        """
        ---
        delete:
          summary: Delete item from cart
          description: Remove a product from the cart by product_id.
          parameters:
            - in: path
              name: cart_id
              required: true
              description: Cart identifier (user or session id)
              schema:
                type: string
          requestBody:
            required: true
            content:
              application/json:
                schema: DeleteItemSchema
          responses:
            200:
              description: Item removed or was not present, updated cart returned
              content:
                application/json:
                  schema: CartResponseSchema
        """
        product_id = data["product_id"]
        cart = _service.delete_item(cart_id, product_id)
        return cart
