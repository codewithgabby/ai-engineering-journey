# Day 35 — One-to-Many Relationships

## What I Learned

A one-to-many relationship means one record can be connected to many records.

Example:

Category → Products

One category can contain many products, while each product belongs to one category.

## Database Relationship

The foreign key is stored on the "many" side:

Product.category_id → Category.id

## SQLAlchemy Relationship

```python
class Category(Base):
    products = relationship(
        back_populates="category"
    )

class Product(Base):
    category_id = mapped_column(
        ForeignKey("categories.id"),
        nullable=True
    )

    category = relationship(
        back_populates="products"
    )