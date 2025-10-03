"""
Cart service providing business logic for cart operations.

This layer separates application logic from routing and persistence concerns.
"""

from typing import Dict

from app.data.cart_repository import InMemoryCartRepository


class CartService:
    """Service for handling cart actions."""

    def __init__(self, repository: InMemoryCartRepository | None = None) -> None:
        self.repository = repository or InMemoryCartRepository()

    # PUBLIC_INTERFACE
    def view_cart(self, cart_id: str) -> Dict:
        """Return the current state of the cart."""
        cart = self.repository.get_cart(cart_id)
        return cart.to_dict()

    # PUBLIC_INTERFACE
    def add_item(self, cart_id: str, product_id: str, quantity: int) -> Dict:
        """Add an item to the cart and return updated cart."""
        cart = self.repository.get_cart(cart_id)
        cart.add_item(product_id, quantity)
        self.repository.save_cart(cart)
        return cart.to_dict()

    # PUBLIC_INTERFACE
    def delete_item(self, cart_id: str, product_id: str) -> Dict:
        """Delete an item from the cart and return updated cart."""
        cart = self.repository.get_cart(cart_id)
        cart.remove_item(product_id)
        self.repository.save_cart(cart)
        return cart.to_dict()
