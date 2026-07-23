# Database Fundamentals

## Introduction

Today marks the beginning of Week 6: Database Engineering with PostgreSQL and SQLAlchemy.

The focus of today's lesson was understanding why databases exist and how relational databases organize information before writing any SQLAlchemy code.

---

# Why Databases Exist

Python variables only exist while a program is running.

When the application stops, everything stored in memory is lost.

A database provides permanent storage that survives application restarts.

---

# PostgreSQL

PostgreSQL is a Relational Database Management System (RDBMS).

Its responsibilities include:

- storing data
- retrieving data
- updating data
- deleting data
- organizing data
- managing relationships
- supporting multiple concurrent users

---

# Database Structure

A relational database is organized into tables.

Each table stores one type of information.

Example tables:

- products
- customers
- businesses
- sales
- payments

Each table follows the Single Responsibility Principle by storing one category of data.

---

# Columns

Columns describe the attributes of a record.

Example:

- id
- name
- price
- quantity

Columns closely resemble object attributes in Python classes.

---

# Rows

Rows represent individual records.

Example:

One product equals one row.

One customer equals one row.

As a business grows, the number of rows increases while the columns generally remain stable.

---

# CRUD Operations

CRUD represents the four fundamental database operations.

Create → INSERT

Read → SELECT

Update → UPDATE

Delete → DELETE

These operations form the foundation of nearly every backend application.

---

# SQL

SQL (Structured Query Language) is the language used to communicate with relational databases.

Common commands include:

SELECT

INSERT

UPDATE

DELETE

---

# Backend Architecture Connection

FastAPI Router

↓

Service Layer

↓

Repository

↓

SQLAlchemy

↓

SQL

↓

PostgreSQL

Today's lesson completed the missing database piece of the backend architecture studied over the previous weeks.

---

# Key Takeaways

- Databases provide persistence.
- Tables organize related data.
- Columns describe attributes.
- Rows represent records.
- SQL performs CRUD operations.
- FastAPI endpoints eventually translate into SQL operations.
- SQLAlchemy will bridge Python and SQL in future lessons.