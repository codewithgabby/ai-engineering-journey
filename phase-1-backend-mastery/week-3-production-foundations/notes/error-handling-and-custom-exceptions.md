# Error Handling and Custom Exceptions for Backend Systems

**Date:** June 3, 2026
**Phase:** Backend Engineering Mastery
**Week:** 3 – Production Foundations
**Day:** 13

---

# Big Picture

Professional systems assume that things can fail.

Possible failures include:

* invalid user input
* missing data
* database failures
* payment provider failures
* network issues
* file processing errors
* authentication failures
* AI service failures
* external API failures

Good systems are designed around failure.

Mental model:

```text
Failure
↓
Detection
↓
Handling
↓
Recovery
↓
Continue Safely
```

---

# Why Error Handling Exists

Without error handling:

```text
Something Fails
↓
Application Crashes
↓
Users Cannot Continue
```

With error handling:

```text
Something Fails
↓
Handle Failure
↓
Return Meaningful Response
↓
Continue Serving Users
```

Professional applications are designed to fail safely and predictably.

---

# Defensive Programming

Professional engineers constantly ask:

* What could go wrong?
* Where could it fail?
* Who should detect the failure?
* How should the system respond?
* What should the user receive?

Applications should expect failures instead of assuming everything will always work.

---

# Python Exception Handling Flow

```text
try
↓
Did an exception occur?
        ↓
      YES                  NO
       ↓                    ↓
    except               else
       ↓                    ↓
       └─────── finally ─────┘
                 ↓
            Continue Program
```

---

# try

The `try` block contains code that might fail.

Example:

```python
try:
    age = int(input("Age: "))
```

Python attempts to execute the code.

---

# except

The `except` block runs only when an exception occurs.

Example:

```python
try:
    age = int("hello")

except ValueError:
    print("Please enter numbers only.")
```

Flow:

```text
try
↓
Error Occurs
↓
Jump to except
↓
Continue Program
```

---

# else

The `else` block runs only if the `try` block succeeds.

Example:

```python
try:
    age = int("25")

except ValueError:
    print("Invalid input")

else:
    print("Input successful")
```

Flow:

```text
try
↓
Success
↓
Skip except
↓
Run else
```

---

# finally

The `finally` block always runs.

It does not matter whether an error occurred.

Example:

```python
try:
    open_database()

except:
    handle_error()

finally:
    close_database()
```

Flow:

```text
Acquire Resource
↓
Use Resource
↓
Success OR Failure
↓
Always Cleanup
```

---

# Why finally Matters

Professional systems use `finally` for:

* closing database connections
* closing files
* releasing memory resources
* closing network sessions
* cleaning temporary resources
* preventing resource leaks

---

# raise

Sometimes Python cannot know that something is wrong.

Business rules are decided by engineers.

Example:

```python
if amount > balance:
    raise Exception("Insufficient balance.")
```

Flow:

```text
Business Rule Broken
↓
raise
↓
Create Exception
↓
Jump to except
```

---

# Custom Exceptions

Generic exceptions become difficult to manage in large applications.

Professional systems create their own exception types.

Example:

```python
class InsufficientBalanceError(Exception):
    pass
```

Usage:

```python
if amount > balance:
    raise InsufficientBalanceError(
        "Insufficient balance."
    )
```

Examples:

```python
class UserAlreadyExistsError(Exception):
    pass

class PaymentProviderError(Exception):
    pass

class AIModelUnavailableError(Exception):
    pass
```

Benefits:

* readable code
* easier debugging
* self-documenting code
* easier maintenance
* clearer architecture boundaries
* better production monitoring

---

# Architecture Thinking

Typical backend flow:

```text
Request
↓
Router
↓
Service
↓
Repository
↓
Database
```

Failures can happen at any layer.

---

# Router Responsibilities

Responsible for request validation.

Examples:

* invalid email
* missing fields
* invalid request body
* wrong data types

Possible responses:

* 400 Bad Request
* 422 Unprocessable Entity

---

# Service Responsibilities

Responsible for business rules and workflow orchestration.

Examples:

* insufficient balance
* duplicate actions
* permission checks
* payment provider failures
* account restrictions
* AI workflow failures

Service decides how the application should react.

The Service layer commonly raises custom exceptions.

---

# Repository Responsibilities

Responsible for database communication.

Examples:

* queries
* inserts
* updates
* deletes
* database connection failures
* transaction failures

Repository is usually the first layer to notice database problems.

---

# External Provider Failures

Examples:

* payment gateways
* email providers
* SMS providers
* AI APIs
* third-party services

These failures are usually coordinated by the Service layer because the Service orchestrates business workflows.

---

# Production Thinking

Professional systems do not do this:

```text
Failure
↓
Crash
```

Professional systems do this:

```text
Failure
↓
Detect Failure
↓
Handle Failure
↓
Return Meaningful Response
↓
Continue Serving Other Users
```

---

# Architecture Reasoning Framework

Whenever something fails, ask:

```text
Who noticed the problem first?
↓
Who should decide what to do?
↓
What should the user receive?
```

This framework helps engineers reason about failures in large systems.

---

# Backend Example

```text
POST /withdraw
↓
Router
↓
Service
↓
Check Balance
↓
Insufficient Funds
↓
raise InsufficientBalanceError
↓
Exception Handler
↓
Return Response

{
    "detail": "Insufficient balance."
}
```

---

# AI Engineering Connection

The same ideas will later be used in AI systems.

Examples:

```text
Document Upload
↓
Extract Text
↓
Generate Embeddings
↓
Store in Vector Database
↓
LLM Generates Answer
```

Possible failures:

* invalid file
* embedding model unavailable
* vector database offline
* token limit exceeded
* external AI API failure

AI systems must also fail safely and return meaningful responses.

---

# Biggest Takeaway

Exceptions are not only about preventing crashes.

Exceptions help engineers:

* detect failures
* control failures
* communicate failures safely
* protect systems
* protect users
* recover gracefully
* build reliable backend applications
* build reliable AI systems

Production engineering is not about avoiding failures completely.

Production engineering is about designing systems that fail safely, predictably, and recover gracefully.
