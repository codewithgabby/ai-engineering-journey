# Engineering Review and Architecture Thinking

## Purpose of Today's Review

Today was focused on connecting concepts instead of learning completely new topics.

The goal was to understand how multiple backend engineering concepts work together inside real systems.

---

## Concepts Reviewed

### Type Hinting

Type hinting improves:

- readability
- maintainability
- team collaboration
- API development

Type hints help engineers understand expected inputs and outputs clearly.

---

### OOP

Object-oriented programming allows engineers to model real systems using:

- classes
- objects
- methods
- state
- behavior

OOP helps organize backend systems logically.

---

### Inheritance

Inheritance allows child classes to reuse behavior from parent classes.

Benefits:

- code reuse
- shared behavior
- reduced duplication

Example:

```python
class Admin(User)
```

---

### Composition

Composition allows systems to work together.

Example:

```python
UserService has EmailService
```

Benefits:

- modularity
- flexibility
- maintainability

Modern backend systems often prefer composition over large inheritance hierarchies.

---

### Separation of Concerns

Backend systems become easier to maintain when responsibilities are separated.

Common layers:

- routers
- services
- repositories

Each layer should focus on its own responsibility.

---

### Services

Services coordinate business workflows.

Examples:

- user registration
- sales creation
- AI processing
- analytics generation

Services act as the orchestration layer.

---

### Repositories

Repositories interact with storage systems and databases.

Examples:

- save data
- fetch data
- update records
- delete records

Repositories should not contain business logic.

---

### Async Thinking

Async programming improves system responsiveness when waiting for:

- APIs
- databases
- AI services
- file processing

Async allows systems to continue handling work while waiting for responses.

---

## Biggest Realization

Most backend concepts are connected.

When building a real system:

Router
→ Service
→ Repository
→ Database

Additional services such as:

- EmailService
- AIService
- AnalyticsService

can be connected using composition.

This same architecture pattern will later appear in AI systems, RAG systems, and production AI applications.

---

## Engineering Mindset Shift

The goal is no longer just understanding individual lines of code.

The goal is learning how systems are designed, organized, and connected together.