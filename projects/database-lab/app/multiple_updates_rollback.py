from app.database import SessionLocal
from app.models import Product

session = SessionLocal()

beans = session.query(Product).filter(
    Product.id == 3
).first()

oil = session.query(Product).filter(
    Product.id == 4
).first()

if beans is None or oil is None:
    print("One or more products not found")
    session.close()
else:
    print("Original values:")
    print("Beans:", beans.quantity)
    print("Oil:", oil.quantity)

    beans.quantity = 5
    oil.quantity = 25

    print("After changes, before rollback:")
    print("Beans:", beans.quantity)
    print("Oil:", oil.quantity)

    session.rollback()

    print("After rollback:")
    print("Beans:", beans.quantity)
    print("Oil:", oil.quantity)

    session.close()