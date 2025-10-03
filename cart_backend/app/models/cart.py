"""
Cart domain models.

Implements core data structures for cart items and carts, following a clean, modern, and well-documented style.
"""

from dataclasses import dataclass, field
from typing import Dict


@dataclass
class CartItem:
    """Represents an item in the shopping cart."""
    product_id: str
    quantity: int = 1

    def to_dict(self) -> Dict[str, int]:
        """Serialize CartItem into a simple dict."""
        return {"product_id": self.product_id, "quantity": self.quantity}


@dataclass
class Cart:
    """Represents a shopping cart for a specific user/session."""
    cart_id: str
    items: Dict[str, CartItem] = field(default_factory=dict)

    def add_item(self, product_id: str, quantity: int) -> None:
        """
        Add or increment an item in the cart.
        If the item exists, increase its quantity; otherwise, create it.
        """
        if quantity <= 0:
            raise ValueError("Quantity must be greater than zero.")

        if product_id in self.items:
            self.items[product_id].quantity += quantity
        else:
            self.items[product_id] = CartItem(product_id=product_id, quantity=quantity)

    def remove_item(self, product_id: str) -> bool:
        """
        Remove an item from the cart by product_id.
        Returns True if removed, False if not present.
        """
        return self.items.pop(product_id, None) is not None

    def to_dict(self) -> Dict:
        """Serialize Cart into a dict with items."""
        return {
            "cart_id": self.cart_id,
            "items": [item.to_dict() for item in self.items.values()],
            "total_items": sum(i.quantity for i in self.items.values()),
        }
