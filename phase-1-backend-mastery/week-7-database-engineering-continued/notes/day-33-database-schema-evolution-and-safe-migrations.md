# Day 33 — Database Schema Evolution and Safe Migrations

**Date:** July 1, 2026  
**Topic:** Evolving a production database schema safely with Alembic

---

## What We Learned

Today we continued working with Alembic and learned how to safely introduce a new field into an existing database without breaking existing records.

Our `products` table already contained existing products, so adding a new `sku` field required careful migration planning.

The key lesson was:

> Database schema changes must account for the data that already exists.

---

## 1. Adding a New SKU Field

We added `sku` to the `Product` model:

```python
sku: Mapped[str] = mapped_column(String(50), nullable=True)