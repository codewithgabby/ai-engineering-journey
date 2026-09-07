from app.database import SessionLocal
from app.models import Product

session = SessionLocal()

products = session.query(Product).all()

for product in products:
    print(
        product.id,
        product.name,
        product.price,
        product.quantity
    )

session.close()