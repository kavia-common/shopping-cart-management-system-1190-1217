"""
Stub repository for cart persistence.

This module simulates persistence with an in-memory store to satisfy the 'cart_database' dependency.
It is designed with a clear interface so a real database implementation can replace it later without
changing the service layer.
"""

from typing import Dict, Optional
from threading import RLock

from app.models.cart import Cart


class InMemoryCartRepository:
    """
    Thread-safe in-memory repository for carts.
    Not suitable for production but provides a simple stub for development/testing.
    """

    def __init__(self) -> None:
        self._store: Dict[str, Cart] = {}
        self._lock = RLock()

    def get_cart(self, cart_id: str) -> Cart:
        with self._lock:
            return self._store.setdefault(cart_id, Cart(cart_id=cart_id))

    def save_cart(self, cart: Cart) -> None:
        with self._lock:
            self._store[cart.cart_id] = cart

    def delete_cart(self, cart_id: str) -> bool:
        with self._lock:
            return self._store.pop(cart_id, None) is not None

    def find_cart(self, cart_id: str) -> Optional[Cart]:
        with self._lock:
            return self._store.get(cart_id)
