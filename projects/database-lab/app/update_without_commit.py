from app.database import SessionLocal
from app.models import Product

session = SessionLocal()

product = session.query(Product).filter(
    Product.id == 4
).first()

if product is None:
    print("Product not found")
else:
    print("Before update:")
    print(product.price)

    product.price = 25000

    print("After update, before commit:")
    print(product.price)

session.close()