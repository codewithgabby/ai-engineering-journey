# Day 39 — EXPLAIN and EXPLAIN ANALYZE

**Learning timeline:** July 8, 2026  
**Phase:** Phase 1 — Backend Engineering Mastery  
**Week:** Week 9 — Database Engineering  
**Topic:** PostgreSQL Query Plans and Performance Analysis

## 1. The problem this topic solves

A SQL query can return the correct result and still be inefficient.

Imagine a SaaS application with 100,000 products. An endpoint that retrieves a product by ID might respond quickly today, but as the database grows, its performance depends partly on how PostgreSQL locates the requested record.

As backend engineers, we need to understand what the database is doing internally rather than guessing why a query is slow.

PostgreSQL provides two useful tools:

- `EXPLAIN` — shows the query execution plan selected by PostgreSQL.
- `EXPLAIN ANALYZE` — executes the query and reports actual execution statistics alongside the plan.

## 2. What is a query execution plan?

A query execution plan is PostgreSQL's proposed strategy for executing a SQL statement.

For example, when we request a product with a particular ID, PostgreSQL needs to determine how to find that product.

It might scan the table or use an index, depending on the available indexes, table statistics, query conditions, and the planner's estimates.

The database chooses a plan; the engineer examines that plan to understand the work being performed.

## 3. Understanding EXPLAIN

Consider this query:

```sql
SELECT *
FROM products
WHERE id = 1;
```

We can ask PostgreSQL to display its plan:

```sql
EXPLAIN
SELECT *
FROM products
WHERE id = 1;
```

PostgreSQL returns information describing the planned execution steps.

A simplified example might look like this:

```text
Index Scan using products_pkey on products
  Index Cond: (id = 1)
```

This is an illustrative example, not a result measured from our database.

It indicates that PostgreSQL plans to use an index associated with the product's primary key to locate the row.

### Important point

`EXPLAIN` normally plans the statement without executing the underlying query. Some statement types and options have additional behavior, so the exact command matters.

## 4. Understanding EXPLAIN ANALYZE

Now consider:

```sql
EXPLAIN ANALYZE
SELECT *
FROM products
WHERE id = 1;
```

Unlike ordinary `EXPLAIN`, `EXPLAIN ANALYZE` executes the query and reports actual execution measurements.

A simplified example:

```text
Index Scan using products_pkey on products
  (cost=0.15..8.17 rows=1 width=...)
  (actual time=0.020..0.021 rows=1 loops=1)
  Index Cond: (id = 1)
Planning Time: 0.100 ms
Execution Time: 0.050 ms
```

These numbers are illustrative. Actual output varies by database, data, hardware, cache state, and workload.

### How to interpret the output

- `cost` — the planner's estimated cost units, not milliseconds.
- `rows` — the estimated number of rows produced by a plan node.
- `width` — the estimated average row width in bytes.
- `actual time` — observed timing for the plan node, in milliseconds.
- `actual rows` — the number of rows actually produced per loop.
- `loops` — how many times that plan node executed.
- `Planning Time` — time spent planning the statement.
- `Execution Time` — reported execution duration for the statement.

Do not judge a query from one number alone. Compare estimates with actual results, inspect the plan's operations, and consider the query's purpose and workload.

## 5. Sequential scans and index scans

### Sequential scan

A sequential scan reads through a table to find matching rows.

Example plan:

```text
Seq Scan on products
  Filter: (quantity > 0)
```

A sequential scan is not automatically bad. It may be the best choice when a large proportion of the table needs to be read, the table is small, or an index would not be efficient for the query.

### Index scan

An index scan uses an index to locate relevant rows.

Example plan:

```text
Index Scan using products_pkey on products
  Index Cond: (id = 1)
```

An index can be helpful when a query retrieves a small subset of rows. However, indexes consume storage and add work to inserts, updates, and deletes.

**Engineering principle:** Understand the query and its execution plan before deciding whether an index is needed.

## 6. Estimated rows versus actual rows

Suppose PostgreSQL estimates that a query will return 10 rows but the actual result contains 5,000.

That difference may indicate that the planner's estimates do not accurately represent the data distribution.

Possible causes include stale statistics, skewed data, or complex relationships between filter conditions.

Large estimate errors can influence the planner's choice of execution strategy.

This is why `EXPLAIN ANALYZE` is useful: it lets us compare the plan's expectations with observed execution.

## 7. A safe practical workflow

Use a read-only query to begin exploring query plans.

### Step 1 — Inspect the planned query

```sql
EXPLAIN
SELECT *
FROM products
WHERE id = 1;
```

### Step 2 — Inspect actual execution

```sql
EXPLAIN ANALYZE
SELECT *
FROM products
WHERE id = 1;
```

### Step 3 — Examine a broader filter

```sql
EXPLAIN ANALYZE
SELECT *
FROM products
WHERE quantity > 0;
```

### Step 4 — Compare the plans

Ask:

- Did PostgreSQL choose a sequential scan or an index scan?
- How many rows did it estimate?
- How many rows did it actually return?
- Does the plan show a filter or index condition?
- What was the reported execution time?
- Does the plan suggest a real performance problem, or is the query already efficient?

Record the actual output rather than assuming the illustrative plans above will appear in your database.

### Safety warning

`EXPLAIN ANALYZE` executes the statement. Do not use it casually on `UPDATE`, `DELETE`, or other statements that modify data. Those changes can occur even though the command is being used for analysis. Start with `SELECT` statements, and use an appropriate test environment and transaction strategy for write-query experiments.

## 8. Connection to FastAPI

Imagine this endpoint:

```python
@router.get("/products/{product_id}")
def get_product(product_id: int, db: Session = Depends(get_db)):
    statement = select(Product).where(Product.id == product_id)
    return db.scalar(statement)
```

The endpoint's response time includes more than database execution. It can also include network overhead, connection acquisition, Python processing, serialization, and other application work.

If the endpoint becomes slow, the query plan can help determine whether database execution is part of the problem.

A disciplined debugging process is:

1. Reproduce the slow request.
2. Identify the SQL statement being executed.
3. Examine the database execution plan.
4. Compare estimated and actual row counts where appropriate.
5. Investigate indexes, filters, joins, and data distribution.
6. Measure again after any change.

Do not assume every slow API response is caused by a missing database index.

## 9. Common mistakes

- Assuming a sequential scan always means poor performance.
- Treating planner cost units as milliseconds.
- Assuming an index is always faster.
- Ignoring the difference between estimated and actual rows.
- Running `EXPLAIN ANALYZE` on a destructive query without understanding its effects.
- Optimizing a query without measuring the original behavior.
- Looking only at database execution time when the entire API request is slow.

## 10. Key takeaways

- `EXPLAIN` helps us inspect PostgreSQL's chosen plan.
- `EXPLAIN ANALYZE` executes the statement and reports actual measurements.
- Sequential scans and index scans are execution strategies, not automatic indicators of good or bad performance.
- Estimated and actual row counts help us understand planner accuracy.
- Performance improvements should be supported by measurements.
- Query-plan analysis is one tool within a broader backend debugging process.

## 11. Practical follow-up

When revisiting this topic in the database lab:

- [ ] Run `EXPLAIN` against a simple `SELECT`.
- [ ] Run `EXPLAIN ANALYZE` against the same query.
- [ ] Record the plan PostgreSQL actually returns.
- [ ] Identify the scan type.
- [ ] Compare estimated rows with actual rows.
- [ ] Repeat with a different filter.
- [ ] Write down what changed and what did not.

**Completion note:** These notes document the Day 39 roadmap topic. The practical checklist should only be marked complete after the experiments have actually been performed.