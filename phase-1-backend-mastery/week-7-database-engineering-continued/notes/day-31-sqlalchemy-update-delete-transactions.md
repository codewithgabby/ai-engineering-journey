# Day 31 — SQLAlchemy UPDATE, DELETE & Transactions

**Date:** June 29, 2026  
**Phase:** Phase 1 — Backend Engineering Mastery  
**Week:** Week 7 — Database Engineering Continued  
**Focus:** UPDATE, DELETE, commit, and rollback

---

## Today's Goal

Learn how to modify and delete PostgreSQL records using SQLAlchemy ORM while understanding transaction control.

---

## UPDATE

Retrieve a record:

    product = session.query(Product).filter(
        Product.id == 4
    ).first()

Modify it:

    product.price = 20000

Persist the change:

    session.commit()

Changing the Python object does not permanently persist the change by itself. The transaction must be committed.

---

## DELETE

Find the record:

    product = session.query(Product).filter(
        Product.id == 5
    ).first()

Delete it:

    session.delete(product)

Persist the deletion:

    session.commit()

---

## Transactions

A SQLAlchemy session manages database work within a transaction.

    session.commit()

Persists the transaction.

    session.rollback()

Discards uncommitted changes.

---

## Multiple Changes

Multiple changes can be made before one commit:

    beans.quantity = 10
    oil.quantity = 45

    session.commit()

Both changes are committed together.

If rollback is used:

    beans.quantity = 5
    oil.quantity = 25

    session.rollback()

Both uncommitted changes are discarded.

---

## Defensive Database Operations

Queries may return `None`.

Handle missing records before updating or deleting:

    if product is None:
        print("Product not found")
    else:
        session.delete(product)
        session.commit()

---

## Key Engineering Lessons

- UPDATE modifies existing records.
- DELETE removes records.
- `commit()` persists transaction changes.
- `rollback()` discards uncommitted changes.
- Multiple changes can belong to one transaction.
- Missing records must be handled safely.
- Transactions help maintain consistent database state.

---

## FastAPI Connection

These operations will eventually support endpoints such as:

    PUT /products/{product_id}

    PATCH /products/{product_id}

    DELETE /products/{product_id}

Router
↓
Service
↓
SQLAlchemy Session
↓
PostgreSQL