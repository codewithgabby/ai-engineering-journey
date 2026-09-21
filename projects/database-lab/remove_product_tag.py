from app.database import SessionLocal
from app.models import Product, Tag


db = SessionLocal()

try:
    laptop = db.query(Product).filter(
        Product.sku == "LAPTOP-001"
    ).first()

    office = db.query(Tag).filter(
        Tag.name == "Office"
    ).first()

    print("Before:")
    for tag in laptop.tags:
        print("-", tag.name)

    laptop.tags.remove(office)

    db.commit()

    print("\nAfter:")
    for tag in laptop.tags:
        print("-", tag.name)

finally:
    db.close()