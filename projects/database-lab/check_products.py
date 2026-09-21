from app.database import SessionLocal
from app.models import Product


db = SessionLocal()

try:
    products = db.query(Product).all()

    print("Products in database:")

    for product in products:
        print(product.id, product.name, product.sku)

finally:
    db.close()