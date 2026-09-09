# Day 31 Experiment — UPDATE, DELETE & Transactions

**Date:** June 29, 2026

---

## Experiment 1 — UPDATE

Updated Product ID 4:

    product.price = 20000
    session.commit()

Result:

    Oil
    18000 → 20000

Verified the change using a new database query.

---

## Experiment 2 — UPDATE Without Commit

Changed:

    product.price = 25000

without:

    session.commit()

The session showed:

    25000

After the session closed, PostgreSQL still contained:

    20000

Lesson:

Uncommitted changes are not persisted.

---

## Experiment 3 — ROLLBACK

Changed:

    product.price = 30000

Then:

    session.rollback()

Result:

    30000 → 20000

The uncommitted change was discarded.

---

## Experiment 4 — Multiple Updates

Updated:

    Beans: 15 → 10
    Oil:   50 → 45

Then:

    session.commit()

Both changes were persisted.

---

## Experiment 5 — Multiple Updates + ROLLBACK

Changed:

    Beans: 10 → 5
    Oil:   45 → 25

Then:

    session.rollback()

Result:

    Beans → 10
    Oil   → 45

Both uncommitted changes were discarded.

---

## Experiment 6 — DELETE

Deleted Product ID 5:

    Indomie

Using:

    session.delete(product)
    session.commit()

Verified that Product ID 5 was removed from PostgreSQL.

---

## Experiment 7 — DELETE Missing Record

Attempted to delete Product ID 999.

Result:

    Product not found

No exception occurred.

---

## Key Takeaways

    UPDATE
        ↓
    modify object
        ↓
    commit

    DELETE
        ↓
    session.delete()
        ↓
    commit

    Failure or unwanted changes
        ↓
    rollback
        ↓
    discard uncommitted changes