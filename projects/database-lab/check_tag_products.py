from app.database import SessionLocal
from app.models import Tag


db = SessionLocal()

try:
    electronics = db.query(Tag).filter(
        Tag.name == "Electronics"
    ).first()

    print("Electronics products:")

    for product in electronics.products:
        print("-", product.name, product.sku)

finally:
    db.close()