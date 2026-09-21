from sqlalchemy import text

from app.database import SessionLocal


db = SessionLocal()

try:
    result = db.execute(
        text("SELECT product_id, tag_id FROM product_tags")
    )

    rows = result.fetchall()

    print("Product-tag relationships:")

    for row in rows:
        print(row)

finally:
    db.close()