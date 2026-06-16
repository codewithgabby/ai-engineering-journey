# Dependency Injection and Scalable Backends

## What is Dependency Injection?

Dependency Injection (DI) is a design pattern where a class does not create its own dependencies. Instead, dependencies are provided to the class from outside.

Instead of:

```python
class UserService:
    def __init__(self):
        self.email_service = EmailService()
```

we do:

```python
class UserService:
    def __init__(self, email_service):
        self.email_service = email_service
```

The dependency is created elsewhere and injected into the service.

---

## Why Engineers Use Dependency Injection

Dependency Injection helps engineers build systems that are:

- easier to maintain
- easier to test
- easier to scale
- easier to extend
- less tightly coupled

Professional systems are designed to expect change.

---

## Composition vs Dependency Injection

### Composition

Composition answers:

> Which systems work together?

Example:

```text
UserService
    ↓
EmailService
```

Read as:

```text
UserService HAS an EmailService
```

Composition focuses on collaboration between objects.

---

### Dependency Injection

Dependency Injection answers:

> How did UserService receive EmailService?

Example:

```python
email = EmailService()
user = UserService(email)
```

The dependency is created outside and then passed into the class.

---

## Loose Coupling

Loose coupling means that a class is not permanently tied to one implementation.

Example:

```python
user = UserService(EmailService())
user = UserService(SMSService())
user = UserService(WhatsAppService())
```

The same UserService can work with different implementations.

This improves:

- maintainability
- scalability
- flexibility
- production safety

---

## Why Hardcoded Dependencies Become Problems

Bad example:

```python
class PaymentService:
    def __init__(self):
        self.stripe = StripePaymentProvider()
```

Problems:

- difficult to replace providers
- harder to test
- requires more code changes
- creates maintenance risks
- increases production complexity

---

## Dependency Injection and Testing

During testing, engineers do not always want:

- real emails
- real payments
- real AI API calls
- real notifications

Instead, fake services can be injected:

```python
class FakeNotificationService:
    def send(self):
        print("Pretending to send notification")
```

This allows engineers to test business logic safely.

---

## Dependency Injection in FastAPI

FastAPI uses dependency injection heavily.

Example:

```python
@app.post("/users")
async def create_user(
    service: UserService = Depends(get_user_service)
):
    pass
```

The router does not create the service itself.

FastAPI injects the dependency automatically.

---

## Dependency Injection in AI Systems

Example:

```text
AIService
    ↓
ModelProvider
```

Possible implementations:

- OpenAI
- Claude
- Gemini
- Local Llama models

The AI service remains mostly unchanged while providers can be swapped.

---

## Engineering Mindset

Professional engineers build systems that depend on capabilities instead of concrete implementations.

Good systems are designed for:

- change
- maintainability
- testing
- scalability
- production evolution

Dependency Injection is one of the core patterns that makes this possible.