# Day 30 — SQLAlchemy READ Operations

**Date:** June 26, 2026  
**Phase:** Phase 1 — Backend Engineering Mastery  
**Week:** Week 6 — Database Engineering with PostgreSQL & SQLAlchemy  
**Focus:** SQLAlchemy READ operations

---

## 1. Today's Goal

Learn how to retrieve data from PostgreSQL using SQLAlchemy ORM.

Today's focus was on understanding how to:

- Retrieve all records
- Filter records
- Retrieve one matching record
- Handle records that do not exist
- Retrieve multiple matching records
- Sort database results
- Limit the number of returned records

The goal was not just to memorize SQLAlchemy methods, but to understand what is happening between Python, SQLAlchemy, and PostgreSQL.

---

# 2. Core Mental Model

The database READ flow is:

Python Code
↓
SQLAlchemy Session
↓
SQLAlchemy Query
↓
SQL
↓
PostgreSQL
↓
Database rows
↓
SQLAlchemy Python objects

SQLAlchemy allows database rows to be represented as Python objects.

For example:

PostgreSQL row:

    id | name | price | quantity
    ---|------|-------|---------
    4  | Oil  | 18000 | 50

becomes a Python object:

    product.id
    product.name
    product.price
    product.quantity

---

# 3. Retrieving All Records

We used:

    products = session.query(Product).all()

This queries the Product model and retrieves all matching records.

SQLAlchemy generates SQL conceptually similar to:

    SELECT *
    FROM products;

The result is a Python list containing Product objects.

Initially printing the list produced output similar to:

    [<app.models.Product object at 0x...>, ...]

This means SQLAlchemy returned Product instances rather than plain dictionaries.

We then used a loop to inspect their attributes:

    for product in products:
        print(
            product.id,
            product.name,
            product.price,
            product.quantity
        )

---

# 4. Filtering Records

We learned that `.filter()` narrows database results.

Example:

    product = session.query(Product).filter(
        Product.id == 4
    ).first()

This means:

- Query the Product model
- Find records where the ID is 4
- Return the first matching record

Conceptually, SQLAlchemy generates:

    SELECT *
    FROM products
    WHERE id = 4
    LIMIT 1;

The result was:

    4
    Oil
    18000.0
    50

---

# 5. `.first()`

`.first()` returns the first matching result.

Example:

    product = session.query(Product).filter(
        Product.id == 4
    ).first()

Possible outcomes:

Record exists:
    Product object

Record does not exist:
    None

This distinction is extremely important in backend development.

---

# 6. Handling Missing Records

We deliberately queried:

    Product.id == 999

There was no product with that ID.

The result was:

    None

Our original code attempted:

    print(product.id)

Python raised:

    AttributeError: 'NoneType' object has no attribute 'id'

This demonstrated an important defensive programming pattern.

We fixed it with:

    if product is None:
        print("Product not found")
    else:
        print(product.id)
        print(product.name)
        print(product.price)
        print(product.quantity)

Mental model:

    Query
      ↓
    Record exists?
      ├── YES → Product object
      └── NO  → None

A production API should handle the second case instead of crashing.

For example, a future FastAPI endpoint could return an appropriate 404 response.

---

# 7. Filtering by Name

We queried:

    product = session.query(Product).filter(
        Product.name == "Rice"
    ).first()

The database contained two Rice records:

    1 Rice
    2 Rice

Because `.first()` was used, only the first matching Rice was returned.

This demonstrated that:

    .filter()

and:

    .first()

serve different purposes.

`.filter()` determines which records match.

`.first()` determines how many matching records we retrieve.

---

# 8. `.all()` with Filtering

We changed the query to:

    products = session.query(Product).filter(
        Product.name == "Rice"
    ).all()

This returned both Rice records.

Output:

    1
    Rice
    85000.0
    20
    ---
    2
    Rice
    85000.0
    20
    ---

Important distinction:

    .first()
        ↓
    One object or None

    .all()
        ↓
    List of matching objects

---

# 9. Multiple Filter Conditions

We tested:

    products = session.query(Product).filter(
        Product.name == "Rice",
        Product.quantity == 20
    ).all()

This represents an AND condition.

Conceptually:

    WHERE name = 'Rice'
    AND quantity = 20

Both Rice records matched.

This is the foundation for more advanced API search functionality.

---

# 10. Sorting with `order_by()`

We learned how to sort database results.

Ascending:

    products = session.query(Product).order_by(
        Product.price
    ).all()

The result was:

    Indomie    700
    Oil        18000
    Beans      70000
    Rice       85000
    Rice       85000

Conceptually:

    SELECT *
    FROM products
    ORDER BY price ASC;

---

# 11. Descending Order

We imported:

    from sqlalchemy import desc

Then used:

    products = session.query(Product).order_by(
        desc(Product.price)
    ).all()

The result became:

    Rice       85000
    Rice       85000
    Beans      70000
    Oil        18000
    Indomie      700

Conceptually:

    SELECT *
    FROM products
    ORDER BY price DESC;

This is useful for features such as:

- Most expensive products
- Highest-value products
- Highest stock
- Newest records
- Ranking systems

---

# 12. Limiting Results

We combined sorting with limiting:

    products = session.query(Product).order_by(
        desc(Product.price)
    ).limit(3).all()

The result was:

    Rice
    Rice
    Beans

Conceptually:

    SELECT *
    FROM products
    ORDER BY price DESC
    LIMIT 3;

This is important for production systems because we should avoid retrieving unnecessary amounts of data.

Instead of:

    Database
        ↓
    100,000 rows
        ↓
    Python

we can ask the database for:

    Database
        ↓
    ORDER BY
        ↓
    LIMIT 20
        ↓
    Python

This reduces unnecessary data transfer and memory usage.

---

# 13. Current Database Data

At the end of today's experiments, the products table contained:

    ID | Name    | Price | Quantity
    ---|---------|-------|---------
    1  | Rice    | 85000 | 20
    2  | Rice    | 85000 | 20
    3  | Beans   | 70000 | 15
    4  | Oil     | 18000 | 50
    5  | Indomie | 700   | 120

The duplicate Rice records were useful for demonstrating the difference between `.first()` and `.all()`.

---

# 14. Important Engineering Lessons

## Lesson 1 — Don't retrieve unnecessary data

When working with large databases, retrieve only what is needed.

Use:

    filter()
    order_by()
    limit()

appropriately.

---

## Lesson 2 — Database results can be empty

A query may return:

    None

or:

    []

depending on the retrieval method.

Backend code must handle these cases intentionally.

---

## Lesson 3 — `.first()` and `.all()` are different

`.first()`:

    One object or None

`.all()`:

    List of objects

This distinction will become important when building FastAPI endpoints.

---

## Lesson 4 — The database should do database work

Filtering, sorting, and limiting should generally happen at the database level rather than retrieving a huge dataset into Python and processing everything there.

---

# 15. Connection to FastAPI

Today's SQLAlchemy knowledge will eventually support endpoints such as:

    GET /products

    GET /products/{product_id}

    GET /products?name=Rice

    GET /products?name=Rice&quantity=20

    GET /products?limit=20

The architecture will eventually look like:

    HTTP Request
         ↓
    FastAPI Router
         ↓
    Service Layer
         ↓
    SQLAlchemy Session
         ↓
    PostgreSQL
         ↓
    Query / Filter / Sort / Limit
         ↓
    SQLAlchemy Objects
         ↓
    Pydantic Schema
         ↓
    JSON Response

---

# 16. Day 30 Summary

Today we moved from simply storing data to intelligently retrieving it.

We learned:

    .all()
    .first()
    .filter()
    .order_by()
    desc()
    .limit()

We also encountered and fixed a real `NoneType` error.

The most important conceptual progression was:

    READ everything
        ↓
    FILTER
        ↓
    SELECT one/multiple
        ↓
    SORT
        ↓
    LIMIT

This is the foundation for building efficient database-backed APIs.

---

# 17. Next Step

Next database lesson:

**UPDATE and DELETE operations**

We will learn:

- How SQLAlchemy changes existing records
- How transactions protect database changes
- How rollback works
- How to safely delete records
- Why modifying data requires more care than reading it