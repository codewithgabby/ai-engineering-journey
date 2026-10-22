# Day 44 — Database Transaction Boundaries

## 1. What I Learned

A database transaction groups related database changes into one logical unit. If an operation fails before the transaction commits, the database can roll back the uncommitted changes.

This helps prevent inconsistent business states in applications such as Saleszy, where a sale and its inventory update must remain consistent.

## 2. Session vs Transaction

- **SQLAlchemy Session:** The object used to interact with the database and manage ORM state.
- **Transaction:** The unit of database work that can be committed or rolled back.
- **`commit()`:** Commits pending changes.
- **`rollback()`:** Rolls back the current uncommitted transaction.
- **`with db.begin()`:** Manages a transaction context, committing on successful completion and rolling back when an exception escapes.

A session can participate in multiple transactions over its lifetime.

## 3. Experiments Completed

Three isolated experiments demonstrated transaction rollback:

1. A transaction using an SQLAlchemy engine connection.
2. Multiple database operations grouped into one transaction.
3. A transaction using a SQLAlchemy Session.

In each experiment, a database operation failed after an inventory update was attempted. The transaction rolled back, and the inventory quantity remained at its original value of 5.

These experiments used an in-memory SQLite database to demonstrate the concept without changing the application's PostgreSQL data.

## 4. Repository Architecture

The existing `create()`, `update()`, and `delete()` repository functions commit independently.

This is suitable for their current independent CRUD behavior but complicates business operations that need multiple changes to succeed or fail together.

For a service-owned transaction, repository operations must use the same session and avoid committing independently within that workflow.

## 5. Practical Implementation

Added an `update_fields()` helper to `app/repositories/product_repository.py`:

```python
def update_fields(
    db: Session,
    product: Product,
    update_data: dict,
) -> Product:
    for field, value in update_data.items():
        setattr(product, field, value)

    return product
```

The helper modifies the product without committing. The calling service can decide when the transaction should be committed.

The helper assumes the supplied update fields have already been validated and restricted to permitted model fields.

## 6. Verification

The following checks passed:

```bash
python -m compileall -q app
python -c "from app.repositories.product_repository import update_fields; print('Transaction-aware helper import successful')"
```

These checks confirm syntax and importability. The helper has not yet been verified through a database operation or integrated into a service-owned transaction.

## 7. Engineering Takeaway

Transaction ownership should match the business operation. When multiple database changes must remain consistent, the service should coordinate them within one transaction, while repositories perform the individual data operations without independently committing.

## 8. Next Step

Integrate a transaction-aware workflow into the service layer, handle existing session transaction state correctly, and verify the behavior without breaking the existing product CRUD endpoints.