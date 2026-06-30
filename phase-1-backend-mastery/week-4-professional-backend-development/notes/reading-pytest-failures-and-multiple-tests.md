# Reading pytest Failures and Running Multiple Tests

**Date:** June 10, 2026

**Phase:** Backend Engineering Mastery

**Week:** 4 – Professional Backend Development

**Day:** 18

---

# Big Picture

Writing tests is only half of automated testing.

Professional engineers spend a significant amount of time reading failed tests to understand what went wrong and how to fix it.

A failing test is not something to fear.

It is valuable feedback that helps us improve the application.

Mental Model:

Write Test
↓
Run Test
↓
Read Failure Report
↓
Understand the Problem
↓
Fix the Code or the Test
↓
Run Tests Again

---

# Understanding a Failed Test

Example:

```python
def add(a, b):
    return a + b


def test_add_two_numbers():
    assert add(2, 3) == 6
```

The function returns:

5

The test expects:

6

Since they are different:

pytest reports a failure.

---

# Reading a pytest Failure Report

A typical failure report contains:

- the test function that failed
- the exact line where the failure happened
- the actual value
- the expected value
- an AssertionError
- a summary of failed tests

Example:

```
assert 5 == 6
```

This tells us:

Actual Result:

5

Expected Result:

6

The report provides enough information to begin debugging immediately.

---

# Actual Value vs Expected Value

Actual Value:

The value produced by the application.

Expected Value:

The value the test expects.

Example:

```python
assert add(2, 3) == 6
```

Actual:

5

Expected:

6

The mismatch causes the test to fail.

---

# AssertionError

An AssertionError does NOT mean Python crashed.

It simply means:

"The expected result and the actual result are different."

This is one of the most common errors seen while writing automated tests.

---

# Is the Bug in the Code or the Test?

Whenever a test fails, engineers should ask:

1. Is the application behaving incorrectly?

or

2. Is the test expecting the wrong result?

Not every failed test means the application has a bug.

Sometimes the test itself is incorrect.

---

# Multiple Tests

A single file can contain many test functions.

Example:

```python
def test_add_positive_numbers():
    ...

def test_add_zero():
    ...

def test_add_negative_numbers():
    ...
```

pytest automatically discovers every function beginning with:

```
test_
```

Each function is treated as an independent test.

---

# Test Discovery

When running:

```bash
pytest
```

pytest searches the project for:

- files beginning with `test_`
- functions beginning with `test_`

It automatically executes every discovered test.

---

# Multiple Test Results

Example:

Three tests:

PASS

PASS

FAIL

Summary:

2 passed

1 failed

pytest continues running remaining tests even after one test fails.

This allows engineers to discover multiple problems in a single test run.

---

# Business Rules vs Calculations

Testing is not only about arithmetic.

Before calculating results, engineers ask:

Is this operation allowed?

Example:

Withdraw:

-₦500

Instead of calculating:

5000 - (-500)

the application should reject the request because a withdrawal amount cannot be negative.

Good testing verifies business rules, not only mathematical results.

---

# Professional Debugging Questions

Whenever a test fails, ask:

- Which test failed?
- What was the actual value?
- What was the expected value?
- Which line failed?
- Is the bug in the code or in the test?

Following this process makes debugging systematic and efficient.

---

# Backend Engineering Connection

Production backend applications contain hundreds or thousands of automated tests.

Developers rely on pytest to:

- discover tests
- execute tests
- identify failures
- locate bugs
- verify fixes

Reading failure reports is a core backend engineering skill.

---

# Biggest Takeaways

Today I learned that a failed test is not a disaster.

A failed test is information.

pytest provides detailed reports that help engineers locate problems quickly.

I also learned that pytest automatically discovers multiple tests and continues running them even if one fails, allowing developers to identify several issues during a single test run.

Finally, I learned that testing is not only about checking calculations. Good tests also verify business rules and validate that applications reject invalid operations safely.