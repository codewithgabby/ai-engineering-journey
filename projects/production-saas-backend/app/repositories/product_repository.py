
from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models.product import Product


def get_by_id(db: Session, product_id: int) -> Product | None:
    statement = select(Product).where(Product.id == product_id)

    return db.scalar(statement)



def get_all(db: Session) -> list[Product]:
    statement = select(Product)

    return list(db.scalars(statement).all())


def create(db: Session, product: Product) -> Product:
    db.add(product)
    db.commit()
    db.refresh(product)
    return product


def update(
    db: Session,
    product_id: int,
    update_data: dict,
) -> Product | None:
    product = get_by_id(db, product_id)

    if product is None:
        return None

    for field, value in update_data.items():
        setattr(product, field, value)

    db.commit()
    db.refresh(product)

    return product


