# Key Engineering Insights

## Variables in Python

In Python, variables do not really store values directly.

A variable is more like a name or pointer that points to an object somewhere in memory.

That is why two variables can sometimes affect the same data if they are pointing to the same object.

---

## Mutable Objects

Mutable objects are objects that can still be changed after they are created.

Examples:
- list
- dictionary
- set

Because mutable objects can change, they can sometimes create hidden bugs when multiple variables are sharing the same object.

---

## Immutable Objects

Immutable objects cannot be changed after they are created.

Examples:
- int
- string
- tuple
- bool

When an immutable value changes, Python usually creates a completely new object instead of modifying the old one.

Immutable objects are usually safer and easier to predict.

---

## Equality vs Identity

`==` checks whether two objects have the same value or content.

`is` checks whether two variables are pointing to the exact same object in memory.

Two variables may have equal values but still be different objects internally.

---

## Shallow Copy

`.copy()` creates a new outer object, but nested objects inside may still be shared.

This means changing nested data in one object can still affect the other object.

---

## Deep Copy

`copy.deepcopy()` creates a completely separate copy of everything, including nested objects.

This prevents shared-state problems and makes the copied object fully independent from the original one.