# Context Managers and Resource Management

## Big Picture

Backend systems constantly use resources such as:

* files
* database connections
* Redis connections
* API connections
* sockets
* locks
* AI model sessions

These resources are limited and must be released properly after use.

---

## The Problem

Poor resource management can lead to:

* resource leaks
* too many database connections
* server slowdowns
* memory issues
* production outages

Example:

Acquire Resource
→ Use Resource
→ Forget to Release
→ Resources Accumulate
→ System Failure

---

## What is a Context Manager?

A Context Manager is a Python mechanism that automatically manages resources by ensuring proper setup and cleanup.

Mental model:

Acquire Resource
→ Use Resource
→ Automatic Cleanup

---

## The `with` Statement

Example:

```python
with open("notes.txt") as file:
    content = file.read()
```

Execution flow:

Open File
→ Read File
→ Exit Block
→ Close File

The file is automatically closed when the `with` block finishes.

---

## Why `with` Exists

Without Context Manager:

```python
file = open("notes.txt")

try:
    content = file.read()

finally:
    file.close()
```

With Context Manager:

```python
with open("notes.txt") as file:
    content = file.read()
```

Python automatically handles cleanup.

---

## Understanding `open()`

```python
file = open("notes.txt")
```

This creates:

```text
file variable
        ↓
   File Object
        ↓
Actual File on Disk
```

The file object acts as a way for Python to communicate with the actual file.

---

## The Two Special Methods

### `__enter__()`

Runs when entering the `with` block.

Responsible for:

* preparing resources
* acquiring resources
* setup operations

Example:

```python
def __enter__(self):
    print("Database Connected")
    return self
```

---

### `__exit__()`

Runs when leaving the `with` block.

Responsible for:

* cleanup
* releasing resources
* closing connections

Example:

```python
def __exit__(self, exc_type, exc_value, traceback):
    print("Database Closed")
```

---

## Execution Flow

```text
Enter with block
        ↓
    __enter__()
        ↓
Run code inside block
        ↓
Leave with block
        ↓
    __exit__()
        ↓
Continue program execution
```

---

## Context Managers and Exceptions

Even if an exception occurs:

```python
with Database() as db:
    query()
    raise Exception()
```

Execution:

Database Connected
→ Query
→ Exception Occurs
→ Database Closed
→ Exception Propagates

Resource cleanup still happens.

This is the major advantage of Context Managers.

---

## Backend Engineering Applications

Context Managers are commonly used for:

### Files

```python
with open("report.txt") as file:
    data = file.read()
```

### Database Sessions

```python
with Session(engine) as session:
    users = session.query(User).all()
```

### Locks

```python
with lock:
    update_shared_data()
```

### AI Systems

```python
with vector_db_client() as client:
    client.store_embeddings()
```

---

## Production Engineering Takeaway

Professional systems are built around this principle:

Acquire Resource
→ Use Resource
→ Release Resource

Context Managers make backend systems safer because cleanup is guaranteed, even when failures or exceptions occur.

The most important rule from today's lesson:

`__exit__()` always runs.
