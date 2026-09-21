from app.database import SessionLocal
from app.models import Product


db = SessionLocal()

try:
    laptop = db.query(Product).filter(
        Product.sku == "LAPTOP-001"
    ).first()

    print("Laptop tags:")

    for tag in laptop.tags:
        print("-", tag.name)

finally:
    db.close()