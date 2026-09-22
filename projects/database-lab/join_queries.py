from sqlalchemy import select

from app.database import SessionLocal, engine
from app.models import Product, Tag, product_tags


engine.echo = True

db = SessionLocal()

try:
    stmt = (
        select(
            Product.name.label("product_name"),
            Tag.name.label("tag_name"),
        )
        .join(
            product_tags,
            Product.id == product_tags.c.product_id,
        )
        .join(
            Tag,
            product_tags.c.tag_id == Tag.id,
        )
        .where(Product.sku == "LAPTOP-001")
    )

    result = db.execute(stmt)

    for row in result:
        print(row)

finally:
    db.close()