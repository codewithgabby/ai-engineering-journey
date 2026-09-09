from app.database import SessionLocal
from app.models import Product

session = SessionLocal()

product = session.query(Product).filter(
    Product.id == 999
).first()

if product is None:
    print("Product not found")
else:
    session.delete(product)
    session.commit()
    print("Product deleted successfully")

session.close()