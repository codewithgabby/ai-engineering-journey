# Day 30 Experiment — SQLAlchemy READ Operations

**Date:** June 26, 2026

---

## Objective

Practice retrieving and manipulating query results using SQLAlchemy ORM.

---

## Experiment 1 — Retrieve All Products

Code:

    products = session.query(Product).all()

Result:

    Product objects were returned.

We then iterated through the objects to display:

    id
    name
    price
    quantity

---

## Experiment 2 — Find Product by ID

Query:

    product = session.query(Product).filter(
        Product.id == 4
    ).first()

Result:

    4
    Oil
    18000.0
    50

---

## Experiment 3 — Query a Missing Product

Query:

    product = session.query(Product).filter(
        Product.id == 999
    ).first()

Result:

    None

Attempting:

    print(product.id)

caused:

    AttributeError: 'NoneType' object has no attribute 'id'

Lesson:

Database queries can return no result, so application code must handle None safely.

---

## Experiment 4 — Handle Missing Product

We added:

    if product is None:
        print("Product not found")
    else:
        print(product.id)
        print(product.name)
        print(product.price)
        print(product.quantity)

Result:

    Product not found

The program completed without crashing.

---

## Experiment 5 — Filter by Name

Query:

    product = session.query(Product).filter(
        Product.name == "Rice"
    ).first()

Result:

    1
    Rice
    85000.0
    20

The database contained two Rice records, but `.first()` returned only the first matching record.

---

## Experiment 6 — Retrieve All Matching Rice Products

Query:

    products = session.query(Product).filter(
        Product.name == "Rice"
    ).all()

Result:

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

Lesson:

`.first()` returns one matching object.

`.all()` returns a list of matching objects.

---

## Experiment 7 — Multiple Conditions

Query:

    products = session.query(Product).filter(
        Product.name == "Rice",
        Product.quantity == 20
    ).all()

Both Rice records matched the conditions.

Conceptually:

    WHERE name = 'Rice'
    AND quantity = 20

---

## Experiment 8 — Sort by Price Ascending

Query:

    products = session.query(Product).order_by(
        Product.price
    ).all()

Result:

    Indomie    700
    Oil        18000
    Beans      70000
    Rice       85000
    Rice       85000

---

## Experiment 9 — Sort by Price Descending

Import:

    from sqlalchemy import desc

Query:

    products = session.query(Product).order_by(
        desc(Product.price)
    ).all()

Result:

    Rice       85000
    Rice       85000
    Beans      70000
    Oil        18000
    Indomie      700

---

## Experiment 10 — Sort and Limit

Query:

    products = session.query(Product).order_by(
        desc(Product.price)
    ).limit(3).all()

Result:

    Rice       85000
    Rice       85000
    Beans      70000

Conceptual SQL:

    SELECT *
    FROM products
    ORDER BY price DESC
    LIMIT 3;

---

# Key Observations

1. SQLAlchemy returns ORM objects rather than raw database rows.
2. `.filter()` narrows the query.
3. `.first()` returns one result or None.
4. `.all()` returns a list.
5. `.order_by()` controls result ordering.
6. `desc()` produces descending order.
7. `.limit()` prevents unnecessary rows from being returned.
8. Missing database records must be handled safely.
9. Database-side filtering, sorting, and limiting are important for scalable applications.

---

# Engineering Connection

These operations will eventually power FastAPI endpoints such as:

    GET /products
    GET /products/{id}
    GET /products?name=Rice
    GET /products?name=Rice&quantity=20

The database layer is responsible for efficiently retrieving the required data before the result is converted into an API response.