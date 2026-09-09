from app.database import SessionLocal
from app.models import Product

session = SessionLocal()

product = session.query(Product).filter(
    Product.id == 4
).first()

if product is None:
    print("Product not found")
else:
    print("Original price:")
    print(product.price)

    product.price = 30000

    print("Price before rollback:")
    print(product.price)

    session.rollback()

    print("Price after rollback:")
    print(product.price)

session.close()