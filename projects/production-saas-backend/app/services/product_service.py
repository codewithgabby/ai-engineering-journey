
from sqlalchemy.orm import Session

from app.models.product import Product

from app.repositories.product_repository import (
    get_by_id,
    get_all,
    create,
    update,
    delete,
    update_fields,
)


def get_product_by_id(
    db: Session,
    product_id: int,
) -> Product | None:
    return get_by_id(db, product_id)


def get_all_products(db: Session) -> list[Product]:
    return get_all(db)


def create_product(db: Session, product: Product) -> Product:
    return create(db, product)


def update_product(
    db: Session,
    product_id: int,
    update_data: dict,
) -> Product | None:
    return update(db, product_id, update_data)


def update_product_transactionally(
    db: Session,
    product_id: int,
    update_data: dict,
) -> Product | None:
    with db.begin():
        product = get_by_id(db, product_id)

        if product is None:
            return None

        update_fields(db, product, update_data)

    return product



def delete_product(
    db: Session,
    product_id: int,
) -> bool:
    return delete(db, product_id)
