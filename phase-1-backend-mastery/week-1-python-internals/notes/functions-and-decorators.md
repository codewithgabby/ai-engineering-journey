# Functions and Decorators

## First-Class Functions

Today I learned that functions in Python are actual objects.

Functions can:
- be stored inside variables
- be passed into other functions
- be returned from functions

This changed the way I look at functions completely.

---

## Higher-Order Functions

Higher-order functions are functions that:
- receive other functions as arguments
or
- return functions

This is one of the things that makes Python flexible and powerful.

---

## Closures

Closures were difficult at first, but I finally started understanding that a closure is a function that remembers data from its outer function even after the outer function has finished running.

The inner function still remembers variables from the outer scope.

---

## Decorators

Decorators were the biggest topic today.

A decorator is basically:
a function that wraps another function and adds extra behavior without modifying the original function directly.

This made me start understanding how frameworks like FastAPI work internally.

---

## Decorator Execution Flow

One important thing I learned is that decorators secretly wrap functions internally.

The wrapper function runs first before the original function executes.

This is why:
- logging
- authentication
- caching
- middleware

can run before the actual function logic.

---

## Decorators with Arguments

Decorators can also receive configuration values.

This introduced multiple layers of execution:
- configuration
- decorator creation
- wrapper creation
- function execution

This part was harder, but it helped me start understanding how modern frameworks are engineered internally.

---

## *args and **kwargs

*args collects extra positional arguments into tuples.

**kwargs collects keyword arguments into dictionaries.

These are important because professional decorators should be flexible enough to work with different functions and arguments.

---

## Biggest Engineering Realization Today

Functions are not just reusable code blocks.

Functions are actual objects that can:
- move around the system
- be wrapped
- be modified
- be returned
- be dynamically executed

That realization changed the way I now look at Python frameworks.

