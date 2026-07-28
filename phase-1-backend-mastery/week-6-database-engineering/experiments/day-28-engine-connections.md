# Day 28 Engineering Lab

## Objective

Connect FastAPI to PostgreSQL and generate the first SQLAlchemy table.

---

## Experiment 1

Created SQLAlchemy Engine

DATABASE_URL = ...

engine = create_engine(DATABASE_URL)

Observation

The Engine was created successfully.

No SQL queries executed.

No tables created.

---

## Experiment 2

Opened a real database connection

with engine.connect() as connection:

Observation

FastAPI successfully communicated with PostgreSQL.

---

## Experiment 3

Executed SQL

SELECT version();

Returned

PostgreSQL 17.5

Observation

Confirmed that SQLAlchemy successfully executed SQL through PostgreSQL.

---

## Experiment 4

Created Product model

Fields

- id
- name
- price
- quantity

Observation

Creating the model alone did not create a table.

---

## Experiment 5

Executed

Base.metadata.create_all(bind=engine)

Observation

SQLAlchemy automatically generated the products table inside PostgreSQL.

Verified inside pgAdmin.

Columns successfully created:

- id
- name
- price
- quantity

---

## Key Observation

Python model

↓

SQLAlchemy

↓

Generated SQL

↓

PostgreSQL Table

---

## Engineering Reflection

The Product model is only a blueprint.

The table does not exist until SQLAlchemy executes create_all().

The Engine knows how to connect.

The Connection performs communication.

PostgreSQL executes SQL.