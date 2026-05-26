# OOP and Backend System Design

## OOP Feels Different in Backend Engineering

Today’s class made me realize that Object-Oriented Programming is not just about creating random classes like Dog or Cat.

Backend engineers use OOP to model real systems and organize large applications properly.

---

## Classes Are Like System Blueprints

One important thing I understood today is that classes act like blueprints for backend systems.

Example:

```python
class User:
```

This means every user object created from the class should follow the same structure and behavior.

This helps backend systems stay organized and scalable.

---

## Constructors and Object State

I learned more deeply how constructors work using:

```python
__init__()
```

The constructor helps initialize object data when the object is created.

Example:

```python
self.name
self.email
```

This allows every object to carry its own data and state inside memory.

---

## Methods Are Behaviors Attached to Objects

Today I understood that methods are simply functions inside classes.

But more importantly, methods represent behaviors attached directly to objects.

Example:

```python
user1.greet()
```

This feels cleaner and more scalable because the behavior belongs directly to the object itself instead of creating random standalone functions everywhere.

---

## Objects Carry State

One major realization today was that objects can change their internal state.

Example:

```python
self.balance += amount
```

This updates the object’s balance internally.

Before deposit:

```text
5000
```

After deposit:

```text
7000
```

This helped me understand how backend systems constantly update object state in real-world applications like banking systems, payment systems, and user systems.

---

## Validation Logic Protects Backend Systems

Another major thing I learned today is that backend engineers do not trust users or external systems completely.

This is why validation logic is important.

Example:

```python
if amount > self.balance:
```

This prevents invalid operations like withdrawing more money than available.

Without validation, systems can become logically broken or unsafe.

---

## Backend Engineering Is About Protecting Systems

Today’s class made me realize that backend engineering is not only about making code work.

It is also about:

- protecting object state
- validating operations
- maintaining system integrity
- organizing scalable systems
- preventing invalid behavior

---

## Biggest Realization Today

OOP is not just syntax.

It is a way backend engineers model, organize, and protect real systems.