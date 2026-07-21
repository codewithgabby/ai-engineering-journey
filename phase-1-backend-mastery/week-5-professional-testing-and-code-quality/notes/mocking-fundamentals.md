# Mocking Fundamentals

## Introduction

Today I learned the basics of mocking using Python's `unittest.mock` module.

Mocking allows me to replace real external dependencies with fake objects during testing. This makes tests faster, safer, and independent of external systems.

---

# Why Mocking Exists

Many backend applications depend on external services such as:

- Payment gateways (Paystack, Stripe)
- Email providers
- SMS services
- Databases
- AI APIs
- Cloud services

Calling these services during every test would be:

- Slow
- Expensive
- Dependent on internet connectivity
- Unreliable if the external service is unavailable

Mocking solves this by replacing the real service with a fake object.

---

# MagicMock

`MagicMock` is a flexible object that can imitate almost any Python object.

Example:

```python
from unittest.mock import MagicMock

fake_gateway = MagicMock()
```

The mock does not perform any real work until we define its behavior.

---

# Configuring Mock Behavior

We can specify what a mocked method should return.

```python
fake_gateway.charge.return_value = {
    "status": "success"
}
```

Whenever `charge()` is called, the mock returns the dictionary above instead of contacting a real payment gateway.

---

# Business Logic Example

```python
def process_payment(payment_gateway):
    response = payment_gateway.charge(5000)

    if response["status"] == "success":
        return "Subscription Activated"

    return "Payment Failed"
```

The function does not know whether it receives a real payment gateway or a mock.

This makes the function easy to test.

---

# Testing Multiple Scenarios

Using mocks allows one function to be tested under different conditions.

Successful payment:

```python
fake_gateway.charge.return_value = {
    "status": "success"
}
```

Failed payment:

```python
fake_gateway.charge.return_value = {
    "status": "failed"
}
```

No production code changes are required.

---

# Debugging Lesson

I encountered:

NameError

because I created a new test file without importing `MagicMock`.

This reinforced the importance of reading Python tracebacks carefully and identifying the actual root cause instead of guessing.

---

# Engineering Connections

Today's lesson connects to several earlier topics:

- Dependency Injection
- Automated Testing
- Fixtures
- Test Isolation

Mocking works well because dependencies are passed into functions instead of being created inside them.

---

# Key Takeaways

- Mocking replaces real dependencies with fake objects.
- `MagicMock` creates configurable fake objects.
- `return_value` controls what a mocked method returns.
- Mocking keeps unit tests fast, deterministic, and inexpensive.
- One piece of business logic can be tested under many different scenarios by changing only the mock's behavior.