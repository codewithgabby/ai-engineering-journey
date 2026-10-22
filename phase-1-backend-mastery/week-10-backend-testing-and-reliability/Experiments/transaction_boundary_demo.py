
from sqlalchemy import create_engine, text

engine = create_engine("sqlite+pysqlite:///:memory:")

with engine.begin() as connection:
    connection.execute(
        text("CREATE TABLE accounts (name TEXT, balance INTEGER)")
    )
    connection.execute(
        text("INSERT INTO accounts VALUES ('Gabby', 100)")
    )

try:
    with engine.begin() as connection:
        connection.execute(
            text("UPDATE accounts SET balance = 50 WHERE name = 'Gabby'")
        )

        connection.execute(
            text("INSERT INTO missing_table VALUES ('test')")
        )
except Exception as exc:
    print(f"Transaction failed: {type(exc).__name__}")

with engine.connect() as connection:
    balance = connection.execute(
        text("SELECT balance FROM accounts WHERE name = 'Gabby'")
    ).scalar_one()

    print(f"Balance after failed transaction: {balance}")
