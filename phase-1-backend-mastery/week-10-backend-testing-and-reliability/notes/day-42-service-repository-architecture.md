# Day 42 — Service and Repository Architecture

**Date:** Monday, July 13, 2026

## What I Learned

Today, I completed the refactoring of my FastAPI product update and delete endpoints to follow a layered architecture.

- **Router:** Handles HTTP requests and responses.
- **Service:** Connects the router to the repository.
- **Repository:** Handles database operations.
- **PostgreSQL:** Stores the product data.

I learned why separating these responsibilities makes backend applications easier to maintain, test, and extend.

## Practical Implementation

I connected the product update and delete operations through the router, service, and repository layers.

I also learned how the application handles missing products and returns appropriate HTTP status codes.

## Verification

I tested the endpoints using Swagger UI:

- Update existing product — `200 OK`
- Update nonexistent product — `404 Not Found`
- Delete existing product — `204 No Content`
- Retrieve deleted product — `404 Not Found`
- Delete nonexistent product — `404 Not Found`

Python compilation and import checks also passed.

## Key Lesson

Separating responsibilities makes backend code easier to understand and maintain. Manual API testing verifies actual behavior, while automated regression tests help detect future breakages.

## Outstanding Work

- Set up automated regression tests.
- Review database transaction rollback and error handling.
- Verify authorization and business ownership for the multi-tenant application.