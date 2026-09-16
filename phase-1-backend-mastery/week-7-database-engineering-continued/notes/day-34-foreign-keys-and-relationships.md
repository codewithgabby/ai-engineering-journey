## Day 34 — Foreign Keys & Relationships

# Date: July 2, 2026
# Phase: Phase 1 — Backend Engineering Mastery
# Week: Week 7 — Database Engineering Continued

Today I learned how foreign keys create relationships between tables in a relational database.

I created a Category model and connected it to the existing Product model using category_id.

categories.id
      ↑
      │
products.category_id

The foreign key was defined with:

category_id: Mapped[int | None] = mapped_column(
    ForeignKey("categories.id"),
    nullable=True
)

I learned that the foreign key is stored in the products table because each product stores the ID of the category it belongs to.

I used Alembic to create and apply a migration that added the categories table, category_id, and the foreign-key constraint.

I tested the constraint by attempting to create a product with category_id=999. PostgreSQL rejected it with a ForeignKeyViolation because that category did not exist.

I then created an Electronics category and successfully connected a Laptop product to it using category_id=1.

I also learned the difference between a foreign key and a SQLAlchemy ORM relationship:

Foreign Key → database-level integrity and relationship.
relationship() → ORM-level navigation between related Python objects.

I also tested an uncategorized product. Because category_id is nullable, a product can exist without a category.

Key Takeaway

A foreign key is not simply a column containing another record's ID. It is a database constraint that protects the relationship between tables and prevents invalid references.

Category
   │
   │ 1
   │
   │
   │ many
   ↓
Product

This is the foundation for understanding one-to-many relationships, which is the next topic.