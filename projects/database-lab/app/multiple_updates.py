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
    print("Before updates:")
    print("Beans:", beans.quantity)
    print("Oil:", oil.quantity)

    beans.quantity = 10
    oil.quantity = 45

    print("After updates, before commit:")
    print("Beans:", beans.quantity)
    print("Oil:", oil.quantity)

    session.commit()

    print("After commit:")
    print("Beans:", beans.quantity)
    print("Oil:", oil.quantity)

    session.close()