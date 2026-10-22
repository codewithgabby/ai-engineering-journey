
from sqlalchemy import create_engine, text

engine = create_engine("sqlite+pysqlite:///:memory:")


def create_tables():
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


def record_sale():
    with engine.begin() as connection:
        connection.execute(
            text("UPDATE inventory SET quantity = quantity - 2")
        )

        connection.execute(
            text("INSERT INTO missing_table VALUES (2)")
        )


create_tables()

try:
    record_sale()
except Exception as exc:
    print(f"Sale failed: {type(exc).__name__}")

with engine.connect() as connection:
    stock = connection.execute(
        text("SELECT quantity FROM inventory")
    ).scalar_one()

    print(f"Inventory after failed sale: {stock}")
