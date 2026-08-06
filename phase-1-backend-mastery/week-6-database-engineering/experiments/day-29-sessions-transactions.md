# Day 29 Engineering Lab

## Objective

Insert the first records into PostgreSQL using SQLAlchemy ORM.

---

## Experiment 1

Created Session Factory

SessionLocal = sessionmaker(...)

Observation

SessionLocal creates Session objects.

---

## Experiment 2

Created Session

session = SessionLocal()

Observation

A new Session object was created.

---

## Experiment 3

Created Product objects

Products

- Rice
- Beans
- Oil
- Indomie

Observation

Objects existed only in Python memory.

---

## Experiment 4

Added Products

session.add(product)

Observation

Products were tracked by the Session.

Nothing was stored inside PostgreSQL yet.

---

## Experiment 5

Committed Transaction

session.commit()

Observation

SQLAlchemy generated INSERT statements automatically.

Products were stored permanently inside PostgreSQL.

---

## Experiment 6

Refreshed Objects

session.refresh(product)

Observation

SQLAlchemy synchronized the Python objects with PostgreSQL.

Auto-generated IDs became available.

---

## Experiment 7

Closed Session

session.close()

Observation

Database resources were released correctly.

---

## Result

Successfully inserted four products into PostgreSQL.

Verified successful execution through terminal output.

Next experiment:

Reading records using SQLAlchemy queries.