# Day 40 — Database + FastAPI Integration

**Learning timeline:** July 9, 2026  
**Phase:** Phase 1 — Backend Engineering Mastery  
**Project:** Production SaaS Backend  
**Status:** Completed

## 1. Learning objectives

The goal was to connect a FastAPI application to PostgreSQL using SQLAlchemy and build working CRUD endpoints.

By the end of this session, I was able to:

- Connect FastAPI to PostgreSQL.
- Use SQLAlchemy to query and modify database records.
- Define database models and Pydantic schemas.
- Validate incoming API requests.
- Implement CRUD endpoints.
- Handle missing resources with HTTP 404 responses.
- Test API behavior through Swagger UI.

## 2. Application architecture

The application follows this basic request flow:

```text
Client
  |
  v
FastAPI Router
  |
  v
Pydantic Validation
  |
  v
SQLAlchemy Session
  |
  v
PostgreSQL Database
  |
  v
API Response
```

### Main components

- `app/main.py` — creates the FastAPI application and registers the products router.
- `app/database.py` — loads database configuration, creates the SQLAlchemy engine and session factory, and provides the database dependency.
- `app/models/product.py` — defines the SQLAlchemy Product model.
- `app/schemas/product.py` — defines request validation and response schemas.
- `app/routers/products.py` — contains the product API endpoints.
- `alembic/` — manages database schema migrations.
- `.env` — stores environment-specific configuration such as `DATABASE_URL`.

## 3. Database connection and sessions

The database module uses `create_engine()` to configure SQLAlchemy's connection to PostgreSQL.

`SessionLocal` is a session factory. It creates database sessions that endpoints can use to query, insert, update, and delete records.

The `get_db()` dependency creates a session for a request and closes it in a `finally` block.

```python
def get_db():
    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()
```

**Important distinction:** Closing a session releases its resources. It does not automatically commit unfinished database changes.

The endpoints explicitly call `db.commit()` when a write operation needs to be persisted.

## 4. SQLAlchemy model

The Product model represents the `products` table in PostgreSQL.

Its fields are:

- `id` — primary key.
- `name` — product name, limited to 100 characters.
- `price` — product price.
- `quantity` — available quantity.

The SQLAlchemy model describes how application objects map to database records.

## 5. Pydantic schemas

Three schemas are used:

- `ProductCreate` — validates data submitted when creating a product.
- `ProductUpdate` — validates data submitted when updating a product.
- `ProductResponse` — defines the data returned to API clients.

Validation rules include:

- Product names must contain at least one character and cannot exceed 100 characters.
- Prices must be greater than or equal to zero.
- Quantities must be greater than or equal to zero.

`ConfigDict(from_attributes=True)` allows Pydantic to build a response from a SQLAlchemy object's attributes.

The purpose of separating models from schemas is to distinguish database structure from the API's input and output contracts.

## 6. CRUD endpoints implemented

| Method | Endpoint | Purpose |
|---|---|---|
| POST | `/products/` | Create a product |
| GET | `/products/` | List products |
| GET | `/products/{product_id}` | Retrieve one product |
| PUT | `/products/{product_id}` | Update a product |
| DELETE | `/products/{product_id}` | Delete a product |

### Create

The endpoint converts validated request data into a SQLAlchemy model, adds it to the session, commits the transaction, refreshes the object, and returns the saved product.

### Read

The list endpoint uses `select(Product)` and `db.scalars(...).all()` to retrieve products.

The single-product endpoint filters by ID and returns a 404 response when the product does not exist.

### Update

The endpoint retrieves the existing product, changes its fields, commits the transaction, and refreshes the object before returning it.

### Delete

The endpoint retrieves the product, deletes it through the SQLAlchemy session, and commits the transaction. A successful deletion returns HTTP 204.

## 7. Validation and error handling

The following behaviors were tested:

- Invalid request data produces HTTP 422.
- A product ID that does not exist produces HTTP 404.
- A valid creation request produces HTTP 201.
- A successful read produces HTTP 200.
- A successful deletion produces HTTP 204.

Validation failures are rejected before invalid product data is persisted.

## 8. Practical testing results

Testing was performed through Swagger UI at:

`http://127.0.0.1:8000/docs`

Results:

- Created Laptop with ID `1`.
- Retrieved the product through the list endpoint.
- Confirmed invalid input was rejected with HTTP 422.
- Retrieved Laptop by ID.
- Confirmed that requesting ID `9999` returned HTTP 404.
- Updated Laptop's price from `850000` to `900000`.
- Updated its quantity from `5` to `8`.
- Created Test Mouse with ID `2`.
- Deleted Test Mouse and confirmed that retrieving ID `2` returned HTTP 404.

The Laptop record remained available after the other tests.

**Testing limitation:** These were manual API tests through Swagger UI. Automated regression tests have not yet been established for these endpoints.

## 9. Database migrations

Alembic was configured to manage database schema changes.

The products table migration was applied successfully, and the current migration revision was:

`9a2c17379f01 (head)`

Migrations provide a version-controlled history of database structure changes instead of relying on manual database modifications.

## 10. Engineering lessons

1. FastAPI handles HTTP requests and responses; SQLAlchemy handles database interactions.
2. Pydantic schemas validate API input and define response structure.
3. A database session provides a controlled unit of interaction with the database.
4. Write operations require an explicit transaction commit to persist changes.
5. `db.refresh()` retrieves the persisted state of an object after a commit.
6. HTTP status codes communicate the outcome of an API operation.
7. Database migrations make schema changes repeatable and trackable.
8. Manual testing is useful, but automated tests are needed to catch regressions reliably.

## 11. Current architectural limitation

The product router currently handles HTTP concerns and database operations in the same module.

This is manageable for a small example, but a growing SaaS application benefits from separating responsibilities into:

- **Router layer:** HTTP requests, responses, and status codes.
- **Service layer:** application workflows and business rules.
- **Repository layer:** database queries and persistence operations.
- **Database layer:** SQLAlchemy configuration and session management.

This separation is the focus of Day 41.

## 12. Next lesson

**Day 41 — Service Layer and Repository Layer**

The next step is to refactor the existing application incrementally, preserve the current API behavior, and introduce clearer boundaries between HTTP handling, business logic, and database access.