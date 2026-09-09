from app.database import SessionLocal
from app.models import Product

session = SessionLocal()

product = session.query(Product).filter(
    Product.id == 5
).first()

if product is None:
    print("Product not found")
else:
    print("Product before deletion:")
    print(product.id)
    print(product.name)
    print(product.price)
    print(product.quantity)

    session.delete(product)

    session.commit()

    print("Product deleted successfully")

session.close()