# SQL Fundamentals Exercises

## Exercise 1

Given the following table:

| id | name | price | quantity |
|----|------|-------|----------|
| 1 | Rice | 85000 | 20 |
| 2 | Beans | 70000 | 15 |
| 3 | Oil | 18000 | 50 |

Answer the following questions.

---

### 1. Retrieve every product.

Expected SQL:

SELECT * FROM products;

---

### 2. Add a product.

Product:

Name: Sugar

Price: 95000

Quantity: 12

Expected SQL:

INSERT INTO products
(name, price, quantity)
VALUES
('Sugar', 95000, 12);

---

### 3. Update Beans price to 72000.

Expected SQL:

UPDATE products
SET price = 72000
WHERE id = 2;

---

### 4. Delete Oil.

Expected SQL:

DELETE FROM products
WHERE id = 3;

---

## Reflection Questions

1. Why is a database better than Python variables for storing business data?

2. What is the difference between a table, a row, and a column?

3. Why is the WHERE clause important when using UPDATE and DELETE?

4. How does CRUD map to SQL commands?

5. How do SQL commands relate to FastAPI endpoints?