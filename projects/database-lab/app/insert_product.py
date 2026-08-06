from app.database import SessionLocal
from app.models import Product

# Create a Session
session = SessionLocal()

# Create a Product object
product1 = Product(
    name="Rice",
    price=85000,
    quantity=20
)

product2 = Product(
    name="Beans",
    price=70000,
    quantity=15
)

product3 = Product(
    name="Oil",
    price=18000,
    quantity=50
)

product4 = Product(
    name="Indomie",
    price=700,
    quantity=120
)

# Tell the Session to track it
session.add(product1)
session.add(product2)
session.add(product3)
session.add(product4)

# Save it permanently
session.commit()

# Refresh the object with values from PostgreSQL
session.refresh(product1)
session.refresh(product2)
session.refresh(product3)
session.refresh(product4)

print(product1.id)
print(product1.name)
print(product1.price)
print(product1.quantity)

print(product2.id)
print(product2.name)
print(product2.price)
print(product2.quantity)

print(product3.id)
print(product3.name)
print(product3.price)
print(product3.quantity)

print(product4.id)
print(product4.name)
print(product4.price)
print(product4.quantity)

# Close the Session
session.close()