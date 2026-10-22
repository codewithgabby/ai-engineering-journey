
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker

engine = create_engine("sqlite+pysqlite:///:memory:")
SessionLocal = sessionmaker(bind=engine)

with engine.begin() as connection:
    connection.execute(
        text("CREATE TABLE inventory (quantity INTEGER)")
    )
    connection.execute(
        text("CREATE TABLE sales (quantity INTEGER)")
    )
    connection.execute(
        text("INSERT INTO inventory VALUES (5)")
    )


def record_sale(db):
    with db.begin():
        db.execute(
            text("UPDATE inventory SET quantity = quantity - 2")
        )

        db.execute(
            text("INSERT INTO missing_table VALUES (2)")
        )


with SessionLocal() as db:
    try:
        record_sale(db)
    except Exception as exc:
        print(f"Sale failed: {type(exc).__name__}")

    stock = db.execute(
        text("SELECT quantity FROM inventory")
    ).scalar_one()

    print(f"Inventory after failed sale: {stock}")
