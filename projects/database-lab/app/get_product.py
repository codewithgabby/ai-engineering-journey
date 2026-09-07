from sqlalchemy import desc

from app.database import SessionLocal
from app.models import Product

session = SessionLocal()

products = session.query(Product).order_by(desc(Product.price)).limit(3).all()

if not products:
    print("No products found")
else:
    for product in products:
        print(product.id)
        print(product.name)
        print(product.price)
        print(product.quantity)
        print("---")

session.close()