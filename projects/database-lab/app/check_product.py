from app.database import SessionLocal
from app.models import Product

session = SessionLocal()

product = session.query(Product).filter(
    Product.id == 4
).first()

if product is None:
    print("Product not found")
else:
    print(product.id)
    print(product.name)
    print(product.price)
    print(product.quantity)

session.close()