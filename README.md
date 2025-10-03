# shopping-cart-management-system-1190-1217

Backend: Flask (Shopping Cart API)

Key endpoints:
- GET /docs/          -> Swagger UI
- GET /               -> Health check
- GET /cart/{cart_id} -> View a cart
- POST /cart/{cart_id}/items -> Add item (body: { product_id, quantity })
- DELETE /cart/{cart_id}/items -> Delete item (body: { product_id })

Notes:
- This service uses an in-memory repository as a stub for the cart_database dependency.
- Replace app/data/cart_repository.py with a real database implementation when ready.