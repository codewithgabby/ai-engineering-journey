# Day 27 — SQLAlchemy Engine & First PostgreSQL Connection

## Objective

Understand how a FastAPI application communicates with PostgreSQL using SQLAlchemy and build the first working database connection.

---

# Project

database-lab

---

# Tools Used

- Python
- FastAPI
- PostgreSQL
- pgAdmin
- SQLAlchemy 2.x
- psycopg
- Alembic
- VS Code

---

# Project Structure

database-lab/
│
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── database.py
│   ├── models.py
│   ├── schemas.py
│   └── crud.py
│
├── requirements.txt
└── .env

---

# What is SQLAlchemy Engine?

The Engine is the bridge between Python and PostgreSQL.

Architecture:

FastAPI
    │
    ▼
SQLAlchemy Engine
    │
    ▼
PostgreSQL

---

# Important Understanding

Creating an Engine does NOT immediately connect to PostgreSQL.

Example:

engine = create_engine(DATABASE_URL)

This simply creates an object that knows HOW to connect.

Actual database communication only happens when SQLAlchemy needs to execute a query.

---

# Connection String

Example:

postgresql+psycopg://postgres:password@localhost:5432/database_lab

Meaning:

- postgresql → Database
- psycopg → Driver
- postgres → Username
- password → PostgreSQL password
- localhost → Database server
- 5432 → PostgreSQL port
- database_lab → Database name

---

# Files Created

database.py

Responsible for:

- Engine creation
- Database configuration

main.py

Responsible for:

- FastAPI application
- API endpoints

---

# Current Endpoint

@app.get("/")
def home():
    return {
        "message": "Database Lab",
        "engine": str(engine)
    }

---

# Important Lesson

There is a difference between:

Creating an Engine

↓

Opening a Connection

↓

Executing SQL Queries

These are three different stages.

---

# Engineering Takeaway

Good backend engineers do not memorize SQLAlchemy.

They understand:

- what happens
- when it happens
- why it happens