# Yield Fixtures and Automatic Resource Cleanup

## Introduction

Today I learned how pytest fixtures can automatically perform both setup and cleanup using the `yield` keyword.

This concept builds directly on the context managers (`with` statement) that I learned in Week 3. Both approaches manage the complete lifecycle of a resource by preparing it before use and cleaning it up afterward.

---

# Why Yield Fixtures Exist

Many backend resources require both setup and cleanup.

Examples include:

- database connections
- Redis connections
- API client sessions
- open files
- network sockets
- temporary directories

If these resources are not released correctly, applications may suffer from memory leaks, connection exhaustion, or unstable behavior.

Yield fixtures allow pytest to automatically manage this lifecycle.

---

# Return vs Yield

Using `return`:

```python
@pytest.fixture
def user():
    return {"name": "Gabby"}
```

The fixture immediately finishes after returning the object.

No cleanup code can execute afterward.

---

Using `yield`:

```python
@pytest.fixture
def user():
    print("Setting up...")

    yield {"name": "Gabby"}

    print("Cleaning up...")
```

Execution flow:

Setup

↓

Yield object to the test

↓

Run the test

↓

Resume after `yield`

↓

Cleanup

This allows pytest to automatically perform cleanup after every test.

---

# Yield Fixture Lifecycle

Pytest treats a yield fixture as having two phases.

## Setup Phase

Everything before the `yield` statement.

Examples:

- connecting to PostgreSQL
- opening files
- creating temporary resources
- creating API clients

---

## Cleanup Phase

Everything after the `yield` statement.

Examples:

- closing database connections
- deleting temporary files
- releasing network resources
- stopping background services

Pytest guarantees that cleanup executes after the test completes.

---

# Function Scope vs Module Scope

## Function Scope

```python
@pytest.fixture
```

or

```python
@pytest.fixture(scope="function")
```

Lifecycle:

Setup

↓

Test

↓

Cleanup

↓

Repeat for the next test

Each test receives a completely fresh fixture.

---

## Module Scope

```python
@pytest.fixture(scope="module")
```

Lifecycle:

Setup

↓

Test 1

↓

Test 2

↓

...

↓

Cleanup

The fixture is shared by every test inside the module before cleanup occurs.

---

# Production Backend Example

A database session fixture often looks like this:

```python
@pytest.fixture
def db_session():
    session = SessionLocal()

    yield session

    session.close()
```

This pattern is commonly used in FastAPI applications and allows every test to automatically receive a properly managed database session.

---

# Engineering Connections

Today's lesson connects several concepts learned earlier in the roadmap.

- Context Managers (Week 3)
- Dependency Injection (Week 3)
- Pytest Fixtures (Week 5)
- Fixture Scopes (Week 5)

Yield fixtures combine resource management with dependency injection, making automated tests safer and easier to maintain.

---

# Key Takeaways

- `yield` allows pytest to perform automatic cleanup.
- Everything before `yield` is setup.
- Everything after `yield` is cleanup.
- Cleanup always runs after the test completes.
- Function scope cleans up after every individual test.
- Module scope cleans up after all tests in the module finish.
- Yield fixtures are widely used in production FastAPI projects for managing database sessions and other resources.