from app.database import SessionLocal
from app.models import Product, Tag


db = SessionLocal()

try:
    electronics = Tag(name="Electronics")
    computer = Tag(name="Computer")
    office = Tag(name="Office")

    laptop = Product(
        name="Laptop",
        description="Dell laptop",
        sku="LAPTOP-001",
        price=500000,
        quantity=10,
    )

    keyboard = Product(
        name="Keyboard",
        description="Wireless keyboard",
        sku="KEYBOARD-001",
        price=25000,
        quantity=20,
    )

    laptop.tags = [electronics, computer, office]
    keyboard.tags = [electronics, computer]

    db.add_all([laptop, keyboard])
    db.commit()

    print("Products and tags created successfully.")

finally:
    db.close()