# Day 28 — SQLAlchemy Engine, Connections & First Table

## Objective

Learn how SQLAlchemy communicates with PostgreSQL by understanding the difference between an Engine and a Connection, then create the first database table from a SQLAlchemy model.

---

# Topics Covered

- SQLAlchemy Engine
- Lazy Connections
- Database Connections
- Executing Raw SQL
- SQLAlchemy Models
- Base.metadata.create_all()

---

# Engineering Architecture

Browser
│
▼
FastAPI
│
▼
SQLAlchemy Engine
│
▼
Connection
│
▼
PostgreSQL

---

# Engine vs Connection

Creating an Engine:

engine = create_engine(DATABASE_URL)

does NOT immediately connect to PostgreSQL.

Instead, the Engine stores:

- database type
- username
- password
- host
- port
- database name

The Engine only knows HOW to connect.

---

# Lazy Connection

A real database connection is only opened when SQLAlchemy actually needs one.

Example:

with engine.connect() as connection:

At this point:

Python

↓

Engine

↓

Connection

↓

PostgreSQL

---

# Executing Raw SQL

Example

result = connection.execute(
    text("SELECT version();")
)

This sends SQL directly to PostgreSQL.

Returned value:

PostgreSQL 17.5 ...

---

# Reading Query Results

version = result.scalar()

scalar() extracts a single returned value.

Useful when a query returns exactly one column and one row.

---

# SQLAlchemy Model

class Product(Base):

This is no longer just a Python class.

It becomes a database blueprint.

---

# __tablename__

__tablename__ = "products"

This tells SQLAlchemy to create a table named:

products

---

# Columns

id

Primary Key

name

VARCHAR(100)

price

FLOAT

quantity

INTEGER

---

# Base.metadata.create_all()

Base.metadata.create_all(bind=engine)

This command:

- Finds every model that inherits from Base.
- Reads each model's structure.
- Creates any missing tables in PostgreSQL.
- Does NOT recreate existing tables.
- Does NOT modify existing tables.

---

# Important Difference

create_all()

✔ Creates missing tables.

✖ Does not alter existing tables.

This limitation is the reason Alembic exists.

---

# Engineering Takeaways

Engine

↓

Knows how to connect.

Connection

↓

Actually talks to PostgreSQL.

Model

↓

Blueprint.

create_all()

↓

Builds tables from blueprints.

Alembic

↓

Updates existing database structures safely.