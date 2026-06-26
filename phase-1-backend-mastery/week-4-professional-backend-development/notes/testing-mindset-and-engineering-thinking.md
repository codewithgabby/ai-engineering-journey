# Testing Mindset and Engineering Thinking

**Date:** June 8, 2026

**Phase:** Backend Engineering Mastery

**Week:** 4 – Professional Backend Development

**Day:** 16

---

# Big Picture

Writing code is only half of software engineering.

Professional engineers must also prove that their code works correctly before it reaches users.

Testing builds confidence that software behaves as expected and helps prevent bugs from reaching production.

Mental model:

Write Code
↓
Test Code
↓
Find Bugs Early
↓
Deploy With Confidence

---

# Why Testing Exists

Without testing:

Write Code
↓
Hope It Works
↓
Users Discover Bugs

With testing:

Write Code
↓
Run Tests
↓
Fix Bugs Early
↓
Reliable Software

Testing reduces risk and improves software quality.

---

# Manual Testing

Manual testing means a person performs actions and checks the results.

Example:

* Enter a username and password.
* Click the Login button.
* Verify that login succeeds.

Manual testing is useful but becomes slow and repetitive as applications grow.

---

# Automated Testing

Automated testing allows the computer to verify software behavior.

Instead of checking the application manually every time changes are made, engineers write tests once and run them whenever the code changes.

Benefits:

* faster feedback
* consistent verification
* fewer regressions
* greater confidence during development

---

# Happy Path

The happy path is the normal scenario where the user provides valid input and everything works as expected.

Example:

Balance = ₦10,000

Withdraw = ₦2,000

Expected Result:

Remaining Balance = ₦8,000

Happy path testing confirms that normal functionality works correctly.

---

# Edge Cases

Edge cases are unusual or unexpected situations that could cause software to fail.

Examples:

* withdrawing more than the available balance
* depositing zero
* depositing a negative amount
* empty email field
* invalid email format
* weak password

Professional engineers actively search for edge cases because real users do not always behave as expected.

---

# Thinking Like a Tester

A programmer often asks:

"Does my code work?"

A tester asks:

"How can I break this code?"

This mindset helps identify hidden bugs before users experience them.

---

# Input and Expected Output

Every test case should describe:

Input
↓
Expected Output

Example:

Input:

Email: [gabby@gmail.com](mailto:gabby@gmail.com)

Password: StrongPassword123

Expected Output:

Registration Successful

Another example:

Input:

Email: ""

Expected Output:

Email is required.

Thinking in terms of inputs and expected outputs creates clear, repeatable tests.

---

# Backend Engineering Connection

Backend APIs should be tested for both normal and abnormal behavior.

Examples include:

* successful registration
* duplicate user registration
* invalid request data
* insufficient account balance
* invalid authentication
* missing required fields

Reliable backend systems are designed to handle both expected and unexpected inputs safely.

---

# Biggest Takeaways

Testing is not about proving software is perfect.

Testing is about increasing confidence that software behaves correctly under many different conditions.

Professional engineers do not only test successful scenarios—they intentionally try to break their own software before users do.
