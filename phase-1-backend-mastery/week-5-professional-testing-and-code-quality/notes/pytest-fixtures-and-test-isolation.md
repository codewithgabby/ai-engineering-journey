# Pytest Fixtures and Test Isolation

## Introduction

As backend applications grow, automated tests also grow.

A professional backend project can contain hundreds or even thousands of tests.

Many of those tests require exactly the same setup before they can run.

For example:

- connect to a database
- create a test user
- prepare sample data
- authenticate a user

Writing this setup repeatedly inside every test makes the code difficult to maintain.

Pytest solves this problem using **fixtures**.

---

# What is a Fixture?

A fixture is a function that prepares data or resources before a test runs.

Instead of every test creating its own setup, pytest automatically calls the fixture and passes the prepared object into the test.

A fixture is simply a reusable setup function.

---

# Why Fixtures Matter

Fixtures help us:

- avoid duplicated setup code
- improve readability
- improve maintainability
- keep tests consistent
- make test suites scalable

They are another real-world application of the DRY (Don't Repeat Yourself) principle.

---

# Our First Fixture

```python
import pytest


@pytest.fixture
def user():
    return {
        "name": "Gabby",
        "role": "admin"
    }


def test_user_name(user):
    assert user["name"] == "Gabby"
```

Notice that we never call the `user()` function ourselves.

Pytest automatically detects the fixture and injects its return value into the test function.

---

# How Fixture Injection Works

The execution flow is:

Pytest starts

↓

Finds a test function

↓

Notices the test requires a fixture

↓

Runs the fixture

↓

Receives the returned object

↓

Passes the object into the test

↓

Runs the assertion

---

# Fresh Fixture for Every Test

One of the most important lessons today is that pytest creates a **new fixture instance for every test** by default.

Example:

Test 1

↓

New User

↓

Run Test

-------------------

Test 2

↓

New User

↓

Run Test

Each test receives its own clean environment.

This prevents tests from affecting one another.

This concept is known as **test isolation**.

---

# Why Test Isolation Matters

Imagine one test changes a user's balance.

If another test reused the same object, it could fail even though the application code is correct.

By creating a fresh object for every test, pytest keeps tests:

- independent
- reliable
- predictable

---

# Test Discovery

Pytest only discovers test files that follow its naming conventions.

Correct examples:

- test_login.py
- test_users.py
- test_fixture_experiments.py

Incorrect example:

- fixture_experiments.py

Renaming our file to start with `test_` allowed pytest to discover and execute it.

---

# Output Capture

We added:

```python
print("Setting up user...")
```

When running:

```bash
pytest
```

pytest hid the print statements.

When running:

```bash
pytest -s
```

pytest displayed them.

This demonstrated that pytest captures standard output by default to keep the terminal clean.

---

# Connection to Previous Lessons

Today's lesson connected multiple engineering concepts we have already learned.

- Dependency Injection
- DRY Principle
- Mutable Objects
- Backend Maintainability
- Automated Testing

Fixtures are another example of dependency injection.

Instead of injecting dependencies into an application, pytest injects prepared objects into tests.

---

# Key Takeaways

- Fixtures prepare reusable test setup.
- Pytest automatically injects fixture values into tests.
- Every test receives a fresh fixture by default.
- Test isolation prevents tests from affecting one another.
- Pytest discovers files beginning with `test_`.
- `pytest -s` displays print statements that are normally hidden.
- Fixtures improve scalability, maintainability, and readability.