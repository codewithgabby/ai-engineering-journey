# Fixture Scopes and Resource Sharing

## Introduction

Yesterday, we learned that pytest creates a new fixture for every test by default.

This provides excellent test isolation but may become inefficient when a fixture is expensive to create, such as a database connection or an API client.

Today, we learned how pytest allows us to control how often fixtures are created using **fixture scopes**.

---

# Why Fixture Scopes Exist

Imagine a backend project with thousands of automated tests.

If every test creates a new database connection, the test suite becomes slower and consumes unnecessary resources.

Fixture scopes allow pytest to reuse fixtures when appropriate, improving performance while balancing test isolation.

---

# Default Fixture Scope

The default fixture scope is:

```python
@pytest.fixture
```

or equivalently:

```python
@pytest.fixture(scope="function")
```

A new fixture is created for every test.

Example:

Test 1

↓

New Fixture

-------------------

Test 2

↓

New Fixture

This provides maximum isolation.

---

# Module Scope

```python
@pytest.fixture(scope="module")
```

The fixture is created once for the entire Python module (file).

Example:

Module

↓

One Fixture

↓

Test 1

↓

Test 2

↓

Test 3

This reduces repeated setup and improves performance.

---

# Other Fixture Scopes

Pytest provides four commonly used scopes.

## Function

Runs once per test.

Best when tests modify data.

## Class

Runs once for all test methods inside a test class.

Useful when several related tests share the same setup.

## Module

Runs once for an entire Python file.

Useful for shared setup within a single module.

## Session

Runs once for the entire pytest session.

Useful for expensive resources that can safely be shared.

---

# Performance vs Test Isolation

Choosing a fixture scope is an engineering decision.

Smaller scopes provide better isolation.

Larger scopes improve performance by reducing repeated setup.

Professional engineers balance these two goals depending on the type of resource being shared.

---

# Shared Mutable State

When fixtures share mutable objects, one test can accidentally affect another.

Example:

```python
user["role"] = "guest"
```

If another test expects:

```python
assert user["role"] == "admin"
```

the second test may fail because both tests are sharing the same object.

This is why function scope is safer for mutable data.

---

# When to Use Each Scope

Use **function** scope when:

- testing banking transactions
- modifying database records
- updating user balances
- changing application state

Use **module** scope when:

- sharing read-only configuration
- using immutable data
- reducing repeated setup inside one module

Use **session** scope when:

- creating expensive resources
- loading application configuration
- connecting to services that do not change during testing

---

# Engineering Connection

Today's lesson connects several concepts from earlier weeks.

- Mutable Objects (Week 1)
- Dependency Injection (Week 3)
- Automated Testing (Week 4)
- Fixtures (Week 5)

Fixture scopes demonstrate another real-world example of balancing correctness, performance, and maintainability.

---

# Key Takeaways

- Fixture scopes determine how often pytest creates a fixture.
- Function scope provides maximum test isolation.
- Module scope shares a fixture across one Python file.
- Session scope shares a fixture across the entire test run.
- Shared mutable objects can cause tests to interfere with each other.
- Choosing the correct scope is an engineering design decision, not simply a syntax choice.