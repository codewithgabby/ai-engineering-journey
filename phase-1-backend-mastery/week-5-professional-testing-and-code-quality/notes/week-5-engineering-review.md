# Week 5 Engineering Review

## Introduction

Today concluded Week 5 of the Backend Engineering Mastery roadmap. Instead of introducing a completely new topic, today's session focused on reviewing and connecting all the testing concepts learned throughout the week into one engineering workflow.

The emphasis was on thinking like a backend engineer rather than simply writing tests.

---

# Engineering Workflow

A typical backend request may look like this:

Frontend

↓

FastAPI Route

↓

Business Service

↓

External API (Paystack)

↓

Database

To test this workflow correctly, different testing tools solve different problems.

---

# Testing Concepts Learned

## Pytest

Pytest provides the framework for writing and executing automated tests.

Responsibilities:

- discovering test files
- executing test functions
- reporting failures
- displaying tracebacks

---

## Fixtures

Fixtures eliminate duplicated setup code.

Instead of creating the same objects inside every test, pytest creates them once and injects them into test functions.

Benefits:

- cleaner tests
- reusable setup
- improved maintainability

---

## Fixture Scopes

Function Scope

Creates a new fixture for every individual test.

Provides maximum isolation.

---

Module Scope

Creates one shared fixture for every test inside the module.

Improves performance when resources are expensive to create.

---

## Yield Fixtures

Yield fixtures separate resource management into two phases.

Setup

↓

Yield resource

↓

Run test

↓

Cleanup

This pattern is commonly used for:

- database sessions
- file handling
- Redis connections
- API clients

---

## Mocking

Mocking replaces real external services with fake objects.

Example:

```python
fake_gateway = MagicMock()
```

Instead of contacting Paystack, the mock returns predefined responses.

Example:

```python
fake_gateway.charge.return_value = {
    "status": "success"
}
```

This allows testing multiple business scenarios safely.

---

# Testing Business Logic

The same business logic can be tested with different mocked responses.

Successful payment:

```python
{
    "status": "success"
}
```

Failed payment:

```python
{
    "status": "failed"
}
```

Only the mock changes.

The production code remains unchanged.

---

# Structured Responses

Instead of returning a simple string:

```python
"Subscription Activated"
```

backend functions often return dictionaries.

Example:

```python
{
    "success": True,
    "message": "Subscription Activated",
    "reference": "TXN123456",
    "amount": 5000
}
```

Structured responses provide additional information that can be consumed by frontend applications and other backend services.

---

# Debugging Lessons

This week reinforced reading Python tracebacks carefully.

Important error types:

## NameError

Occurs when Python cannot find a variable or function.

Example:

Missing `MagicMock` import.

---

## KeyError

Occurs when accessing a dictionary key that does not exist.

Example:

```python
result["amount"]
```

when `"amount"` is missing.

---

## AssertionError

Occurs when the actual result does not match the expected result.

The program runs successfully, but the test expectation is incorrect.

---

# Engineering Takeaways

By the end of Week 5, I can:

- write automated tests with pytest
- reuse setup using fixtures
- control fixture lifecycles with scopes
- manage setup and cleanup using yield fixtures
- mock external APIs using MagicMock
- test multiple scenarios without changing production code
- distinguish between runtime errors and test failures
- debug common pytest failures using tracebacks

These concepts form the foundation of professional backend testing.