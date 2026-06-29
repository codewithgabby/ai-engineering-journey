# Introduction to pytest and Automated Testing

**Date:** June 9, 2026

**Phase:** Backend Engineering Mastery

**Week:** 4 – Professional Backend Development

**Day:** 17

---

# Big Picture

As software projects grow, manually checking every feature becomes impossible.

Professional engineers automate testing so the computer can verify that the application still works whenever changes are made.

Instead of asking:

"Did I break something?"

We let the computer answer that question.

Mental Model:

Write Code
↓
Write Tests
↓
Run pytest
↓
Verify Results
↓
Deploy With Confidence

---

# What is pytest?

pytest is a professional Python testing framework.

It automatically discovers, runs, and reports tests written by developers.

Instead of manually checking outputs with print(), pytest compares actual results against expected results.

---

# Why Engineers Use pytest

Without pytest:

Write Code
↓
Run Program
↓
Check Output Manually

With pytest:

Write Code
↓
Run Tests
↓
Computer Verifies Results
↓
PASS or FAIL

Automated testing saves time and reduces human error.

---

# Virtual Environments

Before installing pytest, we created our first virtual environment.

Command:

python -m venv env

Activation (Windows):

env\Scripts\activate

Purpose:

- isolates project dependencies
- prevents version conflicts
- keeps each project independent
- allows reproducible development environments

Professional Python projects always use virtual environments.

---

# Verifying the Python Interpreter

After activation we verified which Python interpreter was being used.

Command:

python -c "import sys; print(sys.executable)"

Output:

env/Scripts/python.exe

This confirmed that Python commands now use the project's isolated environment instead of the global installation.

---

# Installing Packages

Command:

pip install pytest

pip is Python's package manager.

It downloads packages from the Python Package Index (PyPI) and installs them into the active virtual environment.

---

# Dependencies

Installing one package often installs additional packages.

Example:

pytest

depends on

- pluggy
- colorama
- packaging
- pygments
- iniconfig

These packages are called dependencies.

Dependencies are libraries required for another package to function correctly.

---

# Viewing Installed Packages

Command:

pip list

Purpose:

Display every package currently installed inside the active virtual environment.

This helps engineers inspect project environments and verify installed versions.

---

# Writing the First Automated Test

Example:

```python
def add(a, b):
    return a + b


def test_add_two_numbers():
    assert add(2, 3) == 5
```

Important observations:

- test functions must begin with `test_`
- pytest automatically discovers these functions
- `assert` compares expected and actual values
- no print() statements are needed

---

# The assert Statement

assert expresses an expectation.

Example:

assert add(2, 3) == 5

Python evaluates:

Is 5 equal to 5?

If True:

PASS

If False:

FAIL

assert is the foundation of automated testing.

---

# Running Tests

Command:

pytest

pytest automatically:

- searches for test files
- discovers test functions
- executes each test
- reports results

Example output:

1 passed in 0.07s

---

# Understanding pytest Output

Example:

collected 1 item

Meaning:

pytest found one test function.

Example:

test_addition.py . [100%]

The dot (.) represents one successful test.

Final summary:

1 passed

means every discovered test succeeded.

---

# Backend Engineering Connection

Testing is essential for backend systems because APIs must behave consistently even as the codebase grows.

Professional backend engineers write tests for:

- authentication
- payments
- user registration
- business logic
- validation
- database operations

Automated tests reduce bugs before deployment.

---

# Biggest Takeaways

Today marked the transition from thinking like a tester to becoming a developer who writes automated tests.

I learned how professional engineers:

- isolate project environments
- install project dependencies
- verify their tools
- write automated tests
- allow the computer to validate software behavior

This is the foundation for professional backend testing using pytest.