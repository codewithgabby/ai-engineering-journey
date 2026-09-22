# Day 37 — SQL Joins + SQLAlchemy Joins

## What I Learned

Today I learned how SQL JOINs connect data from multiple database tables.

### SQL JOINs
- INNER JOIN returns rows where matching records exist in both tables.
- LEFT JOIN returns all records from the left table, including rows without a matching record.
- Table aliases make queries shorter and easier to read.
- Column aliases make query results clearer.

### Many-to-Many JOIN
I learned how to query:

Product → product_tags → Tag

using multiple JOIN operations.

### SQLAlchemy JOINs
I implemented JOIN queries using SQLAlchemy's `select()` and `.join()`.

I also learned:
- `.where()` for filtering
- `.order_by()` for sorting
- `.label()` for naming returned columns
- SQLAlchemy parameter binding
- `engine.echo = True` to inspect generated SQL

### Database Engineering Remaining Topics — Summary
- Indexes & Query Performance
- EXPLAIN / EXPLAIN ANALYZE
- Transactions & Concurrency Review
- Database Engineering Review

These were summarized rather than studied deeply.

## Next Class

# Database + FastAPI Integration

We will connect:

Client
→ FastAPI
→ Router
→ Service
→ SQLAlchemy
→ PostgreSQL

We will begin with database session management and learn how a FastAPI request gets a PostgreSQL database session.

## Key Engineering Lesson

SQLAlchemy does not replace SQL knowledge.

It helps us construct and execute SQL from Python while giving us an ORM and application-level abstractions.

Understanding the database underneath the abstraction is essential for debugging, performance, and production engineering.