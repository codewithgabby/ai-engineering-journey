# Day 27 Experiment — SQLAlchemy Engine

## Objective

Create the first FastAPI project connected to PostgreSQL.

---

## Tasks Completed

Created database-lab project

Created virtual environment

Installed:

- FastAPI
- SQLAlchemy
- psycopg
- Alembic
- Uvicorn

---

## Created PostgreSQL database

database_lab

---

## Created Engine

DATABASE_URL = "postgresql+psycopg://postgres:*****@localhost:5432/database_lab"

engine = create_engine(DATABASE_URL)

---

## Started FastAPI

Command

uvicorn app.main:app --reload

---

## Tested API

GET /

Result

{
    "message": "Database Lab",
    "engine": "Engine(postgresql+psycopg://postgres:***@localhost:5432/database_lab)"
}

Status

Successful

---

## Experiment Observation

The API worked.

The Engine object was successfully created.

No SQL queries were executed.

No database tables were created.

---

## Prediction Exercise

Question

What happens if PostgreSQL is stopped?

Initial Prediction

The API would fail because the Engine disconnects.

Discussion

The Engine was never connected.

Creating an Engine only prepares the connection information.

Actual communication begins when SQLAlchemy executes a query.

Experiment postponed to Day 28.