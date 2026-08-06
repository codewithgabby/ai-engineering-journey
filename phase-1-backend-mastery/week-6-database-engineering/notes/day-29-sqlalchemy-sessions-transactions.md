# Day 29 — SQLAlchemy Sessions & Transactions

## Objective

Learn how SQLAlchemy Sessions work and perform the first successful INSERT operation into PostgreSQL.

---

# Topics Covered

- Session
- Session Factory (sessionmaker)
- Transactions
- session.add()
- session.commit()
- session.refresh()
- session.close()

---

# Backend Architecture

Python Code
    │
    ▼
Session
    │
    ▼
Engine
    │
    ▼
Connection
    │
    ▼
PostgreSQL

---

# What is a Session?

A Session is the workspace used to communicate with the database.

Every database operation happens through a Session.

Examples:

- Create
- Read
- Update
- Delete

---

# Session Factory

SessionLocal = sessionmaker(...)

SessionLocal is NOT a Session.

It is a factory that creates Sessions whenever they are needed.

Example

session = SessionLocal()

This creates a brand new Session object.

---

# Session Workflow

Create Session

↓

Create Python Object

↓

session.add()

↓

session.commit()

↓

session.refresh()

↓

session.close()

---

# session.add()

session.add(product)

Purpose:

Tell SQLAlchemy to start tracking a Python object.

Important:

The object is NOT yet stored inside PostgreSQL.

---

# session.commit()

Purpose:

Commit the current transaction.

This permanently writes the tracked objects into PostgreSQL.

Without commit()

↓

Nothing is saved.

---

# session.refresh()

Purpose:

Reload the object from PostgreSQL.

Useful because PostgreSQL may generate values such as:

- Primary Keys
- Default Values

Example:

Before commit

Product

id = None

After refresh

Product

id = 5

---

# session.close()

Purpose

Release database resources.

Close the Session.

Prevent unnecessary database connections.

---

# Transaction Analogy

Git

git add .

↓

Staging Area

↓

git commit

↓

Repository

SQLAlchemy

session.add()

↓

Session

↓

session.commit()

↓

PostgreSQL

---

# Engineering Takeaways

Engine

Knows how to connect.

Session

Performs work.

commit()

Makes changes permanent.

refresh()

Synchronizes Python objects with PostgreSQL.

close()

Releases resources.
