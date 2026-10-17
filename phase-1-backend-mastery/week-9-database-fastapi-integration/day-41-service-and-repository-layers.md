# Day 41 — Service and Repository Layers

**Date:** July 10, 2026  
**Phase:** Backend Engineering Mastery  
**Topic:** Separation of concerns in FastAPI

## What I Learned

- **Router:** Handles HTTP requests, responses, and status codes.
- **Service layer:** Coordinates application operations and provides a place for business rules.
- **Repository layer:** Handles database queries and persistence using SQLAlchemy.
- **Database session:** Manages database interactions and transactions.

## Implementation

I introduced service and repository functions for:

- Retrieving one product.
- Retrieving all products.
- Creating a product.
- Beginning the product update operation.

## Testing

- `GET /products/1` — passed.
- `GET /products/9999` — returned the expected 404.
- `GET /products` — passed.
- `POST /products` — created a product successfully, and the product could be retrieved afterward.

## Engineering Takeaway

Separating HTTP handling from database access makes the application easier to maintain, test, and extend.

**Pending:** Connect and test the update operation, then refactor the remaining CRUD operations.