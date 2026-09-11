# Day 32 — Database Migrations with Alembic

## What I Learned

Today I learned how to manage database schema changes using Alembic with SQLAlchemy.

Previously, I used `Base.metadata.create_all()` to create database tables. I learned that this is useful for initial table creation but is not the proper approach for managing schema changes in a production application.

Alembic allows us to track database schema changes through migration files.

## Key Concepts

### 1. Database Constraints

I added constraints to the `Product` model:

- `name` must not be NULL
- `price` must not be negative
- `quantity` must not be negative
- `id` is the primary key

### 2. Alembic

Alembic is a database migration tool commonly used with SQLAlchemy.

It allows us to move the database schema forward and backward in a controlled way.

### 3. Migration Workflow

The workflow is:

SQLAlchemy Model
→ Alembic Autogenerate
→ Migration File
→ Database

I initialized Alembic and configured it to use the application's `DATABASE_URL` from `.env`.

### 4. First Migration

I generated and applied:

`c38de670e9e3` — `add product constraints`

This added the price and quantity check constraints to PostgreSQL.

### 5. Schema Evolution

I then added a `description` field to the `Product` model.

Alembic detected the change and generated:

`c15efd429069` — `add product description`

I successfully applied the migration with:

```bash
alembic upgrade head