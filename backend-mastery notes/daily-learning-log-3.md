## Day 21 — June 15, 2026 (Monday)

Today I started Week 5, which focuses on professional testing and code quality.

The biggest lesson today was understanding pytest fixtures. At first, I thought a fixture was just another function, but I learned that pytest treats it specially. It automatically runs the fixture, receives the returned object, and injects it into the test function without me calling it directly.

One of the most important concepts I learned today was **test isolation**. I initially thought pytest might create one object and share it across all tests, but I discovered that it creates a fresh object for each test by default. This prevents one test from accidentally affecting another, making automated tests more reliable and predictable.

Another interesting discovery was pytest's test discovery system. My first fixture file wasn't executed because it didn't begin with `test_`. After renaming the file to `test_fixture_experiments.py`, pytest immediately discovered and executed both tests successfully.

I also learned that pytest captures print statements by default. Running `pytest` hid my `print()` output, while running `pytest -s` displayed the fixture execution, allowing me to clearly see that the fixture was executed before each test.

Today's lesson also helped me connect several topics from previous weeks. I realized that fixtures are another form of dependency injection, but instead of injecting dependencies into an application, pytest injects prepared objects into tests. This showed me how different backend engineering concepts are connected rather than being isolated topics.

Overall, today's class strengthened my understanding of automated testing, backend maintainability, and professional engineering practices. I'm beginning to see how testing frameworks are designed to support large, scalable projects with thousands of tests.

#################################################  

## Day 22 — June 16, 2026 (Tuesday)

Today I continued Week 5 by learning about fixture scopes in pytest. Yesterday I learned that pytest creates a fresh fixture for every test, but today I discovered that this default behavior is not always the most efficient approach for large backend projects.

I learned that pytest provides different fixture scopes, including function, class, module, and session. Each scope controls how often a fixture is created and reused. The lesson focused on understanding that fixture scope is an engineering decision rather than something to memorize.

One of the biggest ideas today was the trade-off between performance and test isolation. Smaller scopes, such as function scope, provide better isolation because each test receives a fresh object. Larger scopes, such as module or session scope, improve performance by sharing resources, but they also increase the risk of shared mutable state causing tests to affect one another.

I also connected today's lesson with concepts from previous weeks. The discussion about shared dictionaries reminded me of Python mutable objects from Week 1, while fixture injection continued reinforcing dependency injection concepts from Week 3. This showed me that many backend engineering ideas are interconnected rather than isolated topics.

Although fixture scopes are not the most exciting topic, I now understand why they matter in production systems. Large engineering teams must constantly balance correctness, maintainability, and performance when designing automated test suites. This lesson strengthened my understanding of how professional backend engineers make those decisions.

################################################# 

## Day 23 — June 17, 2026 (Wednesday)

Today's lesson focused on one of the most practical pytest concepts so far: yield fixtures. I learned that a fixture can perform both setup and cleanup automatically by using the `yield` keyword instead of `return`.

One of the biggest realizations today was that yield fixtures are very similar to Python context managers that I learned during Week 3. Both approaches manage the complete lifecycle of a resource by preparing it before use and cleaning it up automatically afterward.

Through several experiments, I observed the difference between function scope and module scope. With the default function scope, pytest created a new fixture for every test, performed the setup, ran the test, and immediately executed the cleanup. After changing the fixture to module scope, I saw that pytest created the fixture only once, shared it between both tests, and delayed the cleanup until every test in the module had completed.

I also completed my first production-style testing experiment by replacing a simple dictionary fixture with a simulated database connection. This helped me understand how FastAPI applications manage database sessions during automated testing. The pattern of connecting before the test, yielding the resource, and closing it afterward now makes much more sense.

Today's lesson also reinforced that automated testing is not just about assertions. It is equally important to think about the lifecycle of resources, proper cleanup, performance, and preventing resource leaks. I can now see how pytest fixtures, dependency injection, and context managers all work together to support clean and maintainable backend systems.

################################################# 

## Day 24 — June 18, 2026 (Thursday)

Today's lesson introduced mocking, one of the most important concepts in professional backend testing. I learned that unit tests should focus on verifying my application's logic rather than depending on external services.

Using `MagicMock`, I created a fake payment gateway and configured it to return different responses without making any real API calls. This allowed me to test both successful and failed payment scenarios using the same business logic.

One important realization today was that the business logic did not need to change. Only the mocked response changed, making it possible to verify multiple scenarios safely and quickly.

During the lesson, I also encountered a `NameError` because I created a new test file without importing `MagicMock`. By reading the traceback carefully, I identified the missing import and fixed the issue. This reinforced the importance of debugging methodically instead of guessing.

I now understand that mocking is essential when testing integrations with payment gateways, email services, databases, and AI APIs because it keeps tests fast, predictable, and independent of external systems.

################################################# 

## Day 25 — June 19, 2026 (Friday)

Today marked the completion of Week 5: Professional Testing and Code Quality. Rather than introducing new concepts, today's class focused on connecting everything learned throughout the week into a complete backend testing workflow.

One of the biggest lessons today was understanding how the different testing tools complement one another. Pytest provides the testing framework, fixtures manage reusable setup, yield fixtures handle resource cleanup, fixture scopes control resource lifecycles, and mocking isolates external dependencies from the application's business logic.

I also reinforced why backend services typically return structured dictionaries instead of simple strings. Structured responses allow APIs to communicate additional information such as success status, messages, transaction references, amounts, and other metadata that frontend applications and other services can consume.

During today's review, I practiced reasoning about runtime errors and assertion failures before executing code. I also reviewed common debugging scenarios involving `NameError`, `KeyError`, and `AssertionError`, improving my ability to interpret Python tracebacks and identify root causes efficiently.

Completing Week 5 has given me a much stronger understanding of professional testing practices. I now appreciate that effective testing is not only about writing assertions but also about designing code that is maintainable, testable, and independent of external systems.

This concludes Week 5 of my Backend Engineering Mastery roadmap and prepares me to begin Week 6, where I will focus on PostgreSQL, SQLAlchemy, and production database engineering.

################################################# 

## Day 26 — June 22, 2026 (Monday)

Today marked the beginning of Week 6: Database Engineering with PostgreSQL and SQLAlchemy. Rather than jumping directly into code, I focused on building a strong mental model of how databases fit into backend systems.

I learned why Python variables cannot be used for permanent business data and why relational databases such as PostgreSQL are essential for storing information that must persist even after an application stops running.

I also learned the three core building blocks of a relational database: tables, columns, and rows. Tables store one type of information, columns define the attributes of each record, and rows represent individual records. I connected these concepts to Python classes and object attributes, which helped me understand how SQLAlchemy will later map Python objects to database tables.

Another important concept was CRUD (Create, Read, Update, Delete) and how each operation maps directly to SQL commands: INSERT, SELECT, UPDATE, and DELETE. I also saw how these database operations correspond to REST API endpoints in FastAPI, reinforcing the connection between backend architecture and database engineering.

One of the biggest realizations today was that everything learned over the past several weeks—clean architecture, dependency injection, repositories, and testing—was preparing me for the database layer. The repository pattern now has a concrete purpose: communicating with PostgreSQL.

Today's lesson focused on understanding the "why" behind databases. Beginning tomorrow, I will start working with SQLAlchemy and PostgreSQL in code, building on the strong conceptual foundation established today.

################################################# 

# Day 27 — June 23, 2026

## Topic

SQLAlchemy Engine & First PostgreSQL Connection

---

## What I Learned

Today marked the transition from theory to hands-on backend engineering.

I created a dedicated practice project called `database-lab` instead of using Saleszy so I could experiment freely without affecting a production-style application.

I learned that SQLAlchemy's Engine is not an active database connection. It is an object that stores the information required to communicate with PostgreSQL when a query is eventually executed.

I also learned how a PostgreSQL connection string is structured and what each component represents, including the database type, driver, username, password, host, port, and database name.

---

## Practical Work Completed

- Created a new FastAPI project
- Created a virtual environment
- Installed SQLAlchemy
- Installed psycopg
- Installed Alembic
- Created a PostgreSQL database named `database_lab`
- Built the first `database.py`
- Created the first SQLAlchemy Engine
- Connected FastAPI to the Engine
- Successfully ran the application

---

## Biggest Insight

Creating an Engine does not mean Python is already connected to PostgreSQL.

The Engine simply knows how to establish a connection when SQLAlchemy needs one.

---

## Challenges

Initially, I assumed stopping PostgreSQL would immediately break the application because the Engine would disconnect.

I now understand that the Engine does not establish a database connection until a database operation actually occurs.

---

## Next Session

- Learn SQLAlchemy Sessions
- Execute the first real database connection
- Understand lazy connections
- Create the first Product model
- Create the first database table
- Inspect the table inside pgAdmin

#################################################  

# Day 28 — June 24, 2026

## Topic

SQLAlchemy Engine, Connections & First Database Table

---

## What I Learned

Today I moved beyond creating an SQLAlchemy Engine and learned how SQLAlchemy actually communicates with PostgreSQL.

I learned that creating an Engine does not immediately connect to the database. The Engine simply stores the information required to establish a connection when SQLAlchemy needs one.

I opened my first real database connection using engine.connect() and successfully executed my first SQL statement from Python.

I also created my first SQLAlchemy model (Product) and learned that defining a model does not automatically create a table.

Using Base.metadata.create_all(bind=engine), SQLAlchemy generated my first PostgreSQL table from my Python class.

Seeing the products table appear in pgAdmin helped me connect the relationship between Python models and database tables.

---

## Practical Work Completed

- Connected FastAPI to PostgreSQL
- Opened a real SQLAlchemy Connection
- Executed raw SQL from Python
- Retrieved PostgreSQL version
- Created Product model
- Generated products table automatically
- Verified table inside pgAdmin

---

## Biggest Insight

An Engine is not an active database connection.

A Connection is opened only when SQLAlchemy needs to communicate with PostgreSQL.

A SQLAlchemy Model is only a blueprint until create_all() builds the actual table.

---

## Challenges

Initially I thought creating an Engine immediately established a connection.

After today's experiments I now understand SQLAlchemy's lazy connection behavior.

---

## Engineering Milestone

Today I created my first PostgreSQL table entirely from Python code without manually creating it inside pgAdmin.

This was my first complete ORM workflow.

---

## Next Session

- SQLAlchemy Sessions
- Transactions
- session.add()
- session.commit()
- session.refresh()
- Insert first Product
- View records in pgAdmin
- Query products from PostgreSQL

#################################################  

# Day 29 — June 25, 2026

## Topic

SQLAlchemy Sessions & Transactions

---

## What I Learned

Today I learned how SQLAlchemy Sessions manage communication between Python and PostgreSQL.

I learned that the Engine only knows how to connect to the database, while the Session is responsible for performing actual database operations.

I also learned that session.add() does not immediately save data. Instead, it tells SQLAlchemy to begin tracking the object inside the current Session.

Only after calling session.commit() are the changes permanently written into PostgreSQL.

Finally, I learned that session.refresh() updates my Python object with values generated by PostgreSQL, such as the primary key.

---

## Practical Work Completed

- Created SessionLocal
- Created SQLAlchemy Sessions
- Created multiple Product objects
- Inserted records using session.add()
- Committed transactions
- Refreshed ORM objects
- Printed generated IDs
- Closed database Sessions

---

## Biggest Insight

A Session is similar to Git's staging area.

session.add() tracks changes.

session.commit() permanently saves them.

This analogy helped me understand database transactions much better.

---

## Engineering Milestone

Today I completed my first full CREATE operation using SQLAlchemy ORM.

I successfully inserted multiple products into PostgreSQL without writing raw SQL.

---

## Challenges

Encountered Python package import issues and environment configuration problems.

Debugging these errors improved my understanding of Python packages, module execution, and virtual environments.

---

## Next Session

Engineering Lab 10

CRUD — READ

Topics:

- session.query()
- .all()
- Reading records
- ORM objects
- SQL generated by SQLAlchemy

#################################################  

# June 26, 2026 — Day 30

## Topic
SQLAlchemy READ Operations

## Phase
Phase 1 — Backend Engineering Mastery

## Week
Week 6 — Database Engineering with PostgreSQL & SQLAlchemy

---

## What I Learned Today

Today I learned how to retrieve data from PostgreSQL using SQLAlchemy ORM.

I learned:

- `.all()` to retrieve all matching records
- `.filter()` to narrow database results
- `.first()` to retrieve one matching record
- How `.first()` returns `None` when no record exists
- How to safely handle missing records
- How `.all()` can retrieve multiple matching records
- How to combine multiple filter conditions
- How to sort using `.order_by()`
- How to sort descending using `desc()`
- How to limit database results using `.limit()`

---

## Practical Work

I created and tested SQLAlchemy READ operations against my PostgreSQL `database_lab`.

I successfully retrieved all products and displayed their attributes.

Current product data:

    1 Rice      85000  20
    2 Rice      85000  20
    3 Beans     70000  15
    4 Oil       18000  50
    5 Indomie     700 120

I queried a product by ID and successfully retrieved:

    4
    Oil
    18000.0
    50

I also deliberately queried a product that did not exist:

    Product.id == 999

This returned:

    None

Attempting to access `product.id` caused:

    AttributeError: 'NoneType' object has no attribute 'id'

I then added proper handling using:

    if product is None:

and successfully returned:

    Product not found

---

## Query Experiments

I filtered products by name:

    Product.name == "Rice"

This demonstrated that two Rice records existed.

Using `.first()` returned only the first Rice.

Using `.all()` returned both Rice records.

I then tested multiple conditions:

    Product.name == "Rice"
    Product.quantity == 20

Both Rice records matched.

I also tested sorting:

    order_by(Product.price)

and:

    order_by(desc(Product.price))

Finally, I combined descending sorting with:

    limit(3)

to retrieve only the three most expensive products.

---

## Important Engineering Lesson

One of the biggest lessons today was:

> The database should do as much of the filtering, sorting, and limiting as possible instead of unnecessarily sending large amounts of data to Python.

For example, retrieving 100,000 products just to display the top 10 would be inefficient.

A better approach is:

    PostgreSQL
        ↓
    ORDER BY
        ↓
    LIMIT 10
        ↓
    Python

This reduces unnecessary data transfer and memory usage.

---

## Debugging Lesson

Today's `NoneType` error was useful because it demonstrated a real backend situation.

A database query can legitimately return no record.

Therefore, backend engineers must design for both:

    Record exists

and:

    Record does not exist

This will become especially important when building REST APIs and deciding when to return responses such as HTTP 404.

---

## Systems Thinking Connection

Today's SQLAlchemy operations are the database foundation underneath future FastAPI endpoints.

The eventual architecture will be:

    Client
      ↓
    FastAPI Router
      ↓
    Service
      ↓
    SQLAlchemy Session
      ↓
    PostgreSQL
      ↓
    Query
      ↓
    SQLAlchemy Objects
      ↓
    Pydantic Schema
      ↓
    JSON Response

Understanding the database layer first will make the API layer easier to reason about later.

---

## Today's Progress

I can now:

- Query database records
- Filter records
- Retrieve one record
- Retrieve multiple records
- Handle missing records
- Sort results
- Limit results
- Understand how ORM queries relate to SQL

This moves my understanding beyond simply creating tables and inserting data toward actually working with database-backed application logic.

---

## Next Lesson

Next: **SQLAlchemy UPDATE and DELETE operations**

Focus:

- Updating existing records
- Committing changes
- Transactions
- Rollback
- Safe deletion
- Understanding the risks of modifying persistent data

#############################################################  

# Day 31 — June 29, 2026

## SQLAlchemy UPDATE, DELETE & Transactions

Today I continued my database engineering journey by learning how to modify and safely remove data using SQLAlchemy.

I started by updating an existing product and learned that changing an ORM object's attribute changes its state within the SQLAlchemy session, while session.commit() makes that change persistent in PostgreSQL.

I then tested what happens when an update is made without calling commit(). The change existed temporarily inside the session but was not persisted after the session closed. This helped me understand the difference between changing an object in memory and committing a transaction to the database.

I also practiced session.rollback(). By making changes and then rolling them back, I saw that uncommitted changes could be discarded and the previous committed database state restored.

Another important lesson was that multiple changes can belong to the same transaction. I updated both Beans and Oil and committed them together, then performed another experiment where both changes were rolled back together.

I then learned how to delete records using session.delete() followed by session.commit(). I also practiced safely handling an attempt to delete a product that does not exist instead of allowing the application to crash.

The biggest lesson today was understanding transactions as a unit of database work. I now see that commit() and rollback() are not simply SQLAlchemy commands to memorize; they are tools for controlling whether database changes become permanent or are discarded.

By the end of today's class, I had completed the CRUD cycle and strengthened my understanding of how database changes, transactions, error handling, and backend reliability connect together.

Mental Model

Find Record

↓

Modify or Delete

↓

SQLAlchemy Session Tracks Changes

↓

Commit → Persist Changes

Rollback → Discard Uncommitted Changes

↓

PostgreSQL

↓

Verify Persistent Database State

##############################################################   

# Day 32 — June 30, 2026

# Database Migrations with Alembic

Today I continued database engineering by learning how to manage database schema changes with Alembic.

I started by adding database constraints to the Product model. I made the name field non-nullable and added checks to ensure that price and quantity cannot be negative.

I then learned an important limitation of `Base.metadata.create_all()`. It can create tables, but it does not provide a proper migration history for an evolving production database.

I initialized Alembic and configured it to use the application's DATABASE_URL from the environment file. I connected Alembic's `target_metadata` to the SQLAlchemy `Base.metadata` so that Alembic could compare my models with the actual PostgreSQL database.

I generated my first migration for the product constraints and successfully applied it to PostgreSQL.

After that, I added a description field to the Product model. Alembic detected the new column and generated another migration. I applied the migration successfully and confirmed that the database was at the latest migration:

`c15efd429069 (head)`

The biggest lesson today was understanding that database schema changes need to be tracked just like code changes. Alembic provides a history of these changes and allows the database schema to evolve in a controlled and repeatable way.

Today's mental model is:

SQLAlchemy Model
→ Alembic Migration
→ PostgreSQL Database

This was my first practical introduction to database schema evolution and migration-based database management.

##############################################################   

# Day 33 — July 1, 2026

## Topic
Database Schema Evolution, Data Backfilling, and Unique Constraints with Alembic

## What I Learned

Today I learned how to safely introduce a new field into an existing database using Alembic.

I added a nullable `sku` field to the `Product` model because existing products did not have SKUs. I then generated and applied an Alembic migration to add the column.

After the migration, I backfilled the existing products with unique SKUs:

- Rice → RICE-001
- Rice → RICE-002
- Beans → BEANS-001
- Oil → OIL-001

Before adding the UNIQUE constraint, I checked the database for duplicate SKU values and confirmed that there were none.

I then generated and applied a second migration to make `sku` unique.

Finally, I tested the database constraint by attempting to create a duplicate SKU. PostgreSQL rejected it with a `UniqueViolation`, proving that the constraint was being enforced at the database level.

I also confirmed that a product can still be created with `sku=None`.

## Important Engineering Lesson

I learned that changing a SQLAlchemy model is not the same thing as safely changing a production database.

A safe schema change may require:

```text
Add nullable field
→ migrate
→ backfill existing data
→ validate data
→ add constraint
→ test

########################################################

# Daily Learning Log — Day 34

Date: July 2, 2026
Phase: Phase 1 — Backend Engineering Mastery
Week: Week 7 — Database Engineering Continued
Topic: Foreign Keys & Relationships

Today I learned how foreign keys create relationships between tables in a relational database.

I created a new Category model and connected it to the existing Product model using category_id as a foreign key. I also created and applied an Alembic migration to safely introduce the new categories table and the foreign key constraint.

I learned that a foreign key ensures that a value in one table must correspond to an existing record in another table. I tested this by attempting to create a product with category_id=999, which PostgreSQL correctly rejected with a ForeignKeyViolation.

I then created an actual Electronics category and successfully created a Laptop product connected to it.

I also learned the difference between having a foreign key column and having an ORM relationship. The category_id column stores the actual relationship in the database, while SQLAlchemy's relationship() allows me to navigate between related Python objects, such as:

product.category

Finally, I tested that a product can have no category because category_id is nullable. This helped me understand how optional relationships work.

Key Understanding

Database relationship:

products.category_id → categories.id

The foreign key lives in the products table because each product stores the ID of the category it belongs to.

Engineering Lesson

A foreign key is not just a Python/SQLAlchemy feature. It is a database integrity mechanism. PostgreSQL itself enforces the relationship and prevents invalid references from entering the database.

Day 34 completed: Foreign Keys & Relationships.

###############################################################  

## Day 35 — July 3, 2026

### Topic: One-to-Many Relationships

Today I learned how to model one-to-many relationships with SQLAlchemy and PostgreSQL.

I learned that:
- One Category can have many Products.
- The foreign key (`category_id`) belongs on the many side (`Product`).
- `relationship()` allows SQLAlchemy objects to navigate between related records.
- `back_populates` connects both sides of the ORM relationship.
- `product.category` accesses a product's category.
- `category.products` accesses all products in a category.
- A product can be moved from one category to another through the ORM relationship.
- Setting `product.category = None` removes the product from its category when the foreign key is nullable.
- `flush()` synchronizes pending changes with the database during the transaction.
- `commit()` permanently saves the transaction.

### Engineering Lesson
I learned how database relationships and ORM relationships work together. This is important for designing real backend systems where entities are connected, such as products and categories, users and orders, or customers and transactions.

##############################################    

## Day 36 — July 6, 2026

Today I learned and implemented many-to-many relationships using SQLAlchemy and PostgreSQL.

I created a `Product ↔ Tag` relationship using a `product_tags` association table with two foreign keys and a composite primary key.

I successfully tested creating relationships, accessing them from both directions, and removing a relationship without deleting either entity.

The most important lesson today was debugging. When my first test returned no tags, I checked the actual database and association table instead of assuming the relationship was broken. I discovered that my query had selected the wrong product because there were duplicate product names.

**Key takeaway:** Always verify the actual database state and make sure the test itself is selecting the correct data before changing working code.

##############################################    

# Daily Learning Log — Day 37

## Date
July 7, 2026

## Topic
SQL JOINs + SQLAlchemy JOINs

## Summary

Today I completed the practical study of SQL JOINs and SQLAlchemy JOINs.

I practiced INNER JOIN and LEFT JOIN in PostgreSQL and learned how JOINs combine related records across tables.

I also implemented a many-to-many JOIN between products and tags through the `product_tags` association table.

In SQLAlchemy, I used `select()`, `.join()`, `.where()`, `.order_by()`, and `.label()` and inspected the SQL generated by SQLAlchemy using `engine.echo = True`.

I also reviewed the remaining database-engineering topics at summary level:
- Indexes & Query Performance
- EXPLAIN / EXPLAIN ANALYZE
- Transactions & Concurrency
- Database Engineering Review

## Engineering Insight

Database abstractions are useful, but understanding the SQL underneath them is important for debugging, performance optimization, and production backend engineering.

## Current Progress

Database engineering foundation is substantially complete.

## Next Step

Begin:

**Database + FastAPI Integration**

Starting with:

**FastAPI request → database dependency/session → SQLAlchemy → PostgreSQL → API response**

## Status

Day 37 closed.
Class completed.
Ready for Day 38 / Database + FastAPI Integration.

#######################################################  

Day 38 — Database + FastAPI Integration
Date
July 8, 2026
Topic
Database + FastAPI Integration
What I Worked On
Today I moved from the database engineering lab into the Production-Grade SaaS Backend project.
I created the initial FastAPI project structure and verified that the application runs successfully with Uvicorn and exposes the Swagger documentation.
I connected the new application to PostgreSQL using SQLAlchemy.
Instead of continuing to use the database_lab database, I created a separate production_saas database for the actual application.
Database Integration
Created the SQLAlchemy database configuration with:
- DATABASE_URL
- engine
- SessionLocal
- Base
- get_db()
The get_db() dependency manages the database session lifecycle:
def get_db():    db = SessionLocal()    try:        yield db    finally:        db.close()


Product Model
Created the initial SQLAlchemy Product model containing:
- id
- name
- price
- quantity
Alembic Integration
Initialized Alembic for the Production SaaS Backend.
Configured Alembic to use the application's DATABASE_URL and SQLAlchemy metadata.
Alembic successfully detected the new products table.
Generated migration:
9a2c17379f01_create_products_table.py
The migration was inspected before being applied.
Applied the migration successfully with:
alembic upgrade head

Verified the migration with:
alembic current

Result:
9a2c17379f01 (head)

Engineering Insight
Today marked the transition from isolated database experiments to integrating PostgreSQL into a real FastAPI backend.
The basic architecture is now:
Client
→ FastAPI
→ Database Dependency
→ SQLAlchemy
→ PostgreSQL
The larger architecture we are building toward is:
Router
→ Service
→ Repository
→ SQLAlchemy
→ PostgreSQL
I also reinforced the production habit of inspecting autogenerated migrations before applying them.
Current Status
- FastAPI foundation — Complete
- PostgreSQL connection — Complete
- Database session dependency — Complete
- Product model — Complete
- Alembic setup — Complete
- Initial migration — Complete
- Migration applied and verified — Complete   

###############################################################  

## Day 39 — EXPLAIN / EXPLAIN ANALYZE

**Phase:** Phase 1 — Backend Engineering Mastery  
**Focus:** PostgreSQL Query Performance  
**Status:** Database performance review

### Learning objective

Understand how PostgreSQL query plans help engineers investigate database performance and identify potentially expensive queries.

### Key concepts

- **EXPLAIN:** Displays the execution plan PostgreSQL intends to use for a query.
- **EXPLAIN ANALYZE:** Executes the query and reports actual execution statistics alongside the plan.
- **Query plan:** Describes how PostgreSQL intends to retrieve or modify data.
- **Sequential scan:** Reads rows by scanning a table.
- **Index scan:** Uses an index to locate relevant rows when the planner determines that doing so is appropriate.
- **Estimated cost versus actual execution:** The planner's estimates and the observed execution results provide different kinds of performance information.

### Engineering understanding

Writing a SQL query that returns the correct result is only one part of database engineering. Engineers must also understand how the database executes queries and how performance changes as tables grow.

For example, a query that retrieves one product may work well with a small table but become expensive as the application accumulates many records. Examining the execution plan helps investigate what PostgreSQL is doing instead of relying on guesses.

### Connection to backend engineering

In a FastAPI application, slow database queries can increase endpoint response times, consume database resources, and reduce the number of requests the system can handle efficiently.

Understanding query plans provides a foundation for diagnosing these issues before introducing unnecessary indexes or other optimizations.

### Important lesson

Performance optimization should be based on evidence. An index is not automatically beneficial for every query, and an execution plan must be interpreted in the context of the query, data, and workload.

### Next step

Continue building the PostgreSQL-backed FastAPI application, applying database engineering knowledge to real API operations and later investigating performance where necessary.

################################################################

## Day 40 — Thursday, July 9, 2026
### Topic: Database + FastAPI Integration

**Objective**

Connect the FastAPI application to PostgreSQL and implement a complete set of product CRUD endpoints using SQLAlchemy.

**What I worked on**
- Configured the database connection and SQLAlchemy session dependency.
- Connected the Product model and Pydantic schemas to the API.
- Implemented create, list, retrieve, update, and delete endpoints.
- Used Alembic to manage the products table migration.
- Tested the endpoints through Swagger UI.
- Tested request validation and missing-resource handling.

**Practical results**
- Created and retrieved a Laptop product.
- Confirmed invalid input returned HTTP 422.
- Confirmed a nonexistent product returned HTTP 404.
- Updated the Laptop's price to `900000` and quantity to `8`.
- Created and deleted Test Mouse, then confirmed it could no longer be retrieved.
- Confirmed the Laptop record remained available.

**Key lessons**
- SQLAlchemy sessions manage database interactions.
- Pydantic schemas define and validate the API contract.
- Database changes must be committed to persist.
- Alembic migrations track changes to database structure.
- HTTP status codes communicate the outcome of API requests.
- Separating responsibilities becomes increasingly important as an application grows.

**Engineering reflection**

The API now communicates with PostgreSQL and supports the complete product CRUD workflow. However, the router currently contains both HTTP handling and database logic. This creates an opportunity to improve maintainability by introducing service and repository layers.

**Testing status:** Manual Swagger tests completed. Automated regression tests for these endpoints remain future work.

############################################################   

## Day 41 — July 10, 2026

Today, I learn how to separate my FastAPI application into router, service, and repository layers. I move database operations out of the router and into the repository, while the service coordinates the operations.

I test product retrieval and creation, and the endpoints continue to work as expected. I understand that good backend architecture is not just about making endpoints work; it is also about organizing code so it is easier to maintain, test, and extend.

My next step is to complete the update and delete operations using the same structure.

##################################################################  

### Day 42 — Monday, July 13, 2026

Today, I learned how to separate database operations from the service and router layers in my FastAPI application. I connected the product update and delete operations through the repository, service, and router layers. I tested the endpoints using Swagger UI and confirmed that successful updates return 200, successful deletions return 204, and missing products return 404. I also learned why manual API testing is useful and why automated regression tests are still important. Syntax and import checks passed, but automated tests remain outstanding.