
from sqlalchemy.orm import Session

from app.models.product import Product
from app.repositories.product_repository import get_by_id, get_all, create


def get_product_by_id(
    db: Session,
    product_id: int,
) -> Product | None:
    return get_by_id(db, product_id)


def get_all_products(db: Session) -> list[Product]:
    return get_all(db)


def create_product(db: Session, product: Product) -> Product:
    return create(db, product)