# Day 36 — Many-to-Many Relationships

**Date:** July 6, 2026  
**Week:** Week 8  
**Topic:** Many-to-Many Relationships

## What I Learned

A many-to-many relationship exists when multiple records on both sides can be related.

Example:

Product ↔ Tag

A product can have many tags, and a tag can belong to many products.

We use an association/junction table:

Product
↓
product_tags
↓
Tag

The association table contains:

- `product_id` → `products.id`
- `tag_id` → `tags.id`

Both columns form a composite primary key.

In SQLAlchemy, many-to-many relationships use:

- `relationship()`
- `secondary`
- `back_populates`

I implemented and tested:

- Creating products and tags
- Assigning multiple tags to products
- Accessing tags from products
- Accessing products from tags
- Removing a relationship

### Key Engineering Lesson

When debugging database relationships, verify each layer before changing the implementation.

Our relationship was working correctly; the initial problem was caused by a test query selecting the wrong product because multiple products had the same name.