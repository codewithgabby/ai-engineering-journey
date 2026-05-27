# Inheritance and Composition

## Understanding Inheritance

Today I learned that inheritance allows child classes to reuse behavior from parent classes.

Example:

```python
class Admin(User)
```

This means the Admin class inherits behavior from the User class.

This helps backend engineers avoid rewriting the same code repeatedly.

---

## Parent and Child Relationships

One important thing I understood today is that inheritance creates parent-child relationships between classes.

Example:

```python
User
```

can act as the parent class while:

```python
Admin
Customer
```

can act as child classes.

The child classes automatically inherit shared behavior like:

```python
login()
```

from the parent class.

---

## Shared Backend Behavior

Inheritance is powerful because many backend systems share common behavior.

Example:

- login systems
- authentication
- email handling
- user identity
- permissions

Instead of rewriting these systems repeatedly, engineers place shared behavior inside one parent class.

This creates reusable backend architecture.

---

## Method Overriding

Another important concept I learned today was method overriding.

Example:

```python
class Admin(User):

    def login(self):
```

This allows the Admin class to customize inherited behavior.

This is useful when different systems need specialized functionality.

Example:

- normal user login
- admin login with extra security
- OTP verification
- different permission handling

Overriding allows engineers to reuse architecture while still customizing behavior safely.

---

## Composition

Today I also learned about composition.

Composition means systems work together instead of inheriting everything.

Example:

```python
self.notification_service = NotificationService()
```

This means the User class has a NotificationService.

The User class is not becoming the NotificationService itself.

This creates modular backend architecture.

---

## Separation of Concerns

Composition follows the idea of separation of concerns.

This means every system should handle its own responsibility.

Example:

- NotificationService handles notifications
- User handles user behavior
- PaymentService handles payments

This prevents giant messy classes and improves maintainability.

---

## Why Modern Backend Systems Prefer Composition

One major realization today is that modern backend systems often prefer composition over inheritance when systems become very large.

Composition allows:

- modularity
- flexibility
- scalability
- easier testing
- easier maintenance
- easier replacement of components

This makes large backend systems cleaner and safer.

---

## Biggest Realization Today

Inheritance helps systems reuse behavior through hierarchy.

Composition helps systems collaborate together through modular architecture.

Both are important in scalable backend engineering.