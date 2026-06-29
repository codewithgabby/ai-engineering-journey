# May 18, 2026 — Day 1

Today was actually deeper than I expected. At first, I thought Python variables were just storing values directly, but now I’m beginning to understand that variables are more like references pointing to objects in memory.

One of the biggest things that clicked for me today was mutable vs immutable objects. I finally started seeing why changing one list can unexpectedly affect another variable if both are pointing to the same object. That honestly changed the way I look at Python internally.

The shallow copy vs deep copy part was also very interesting and a little tricky at first. I initially thought `.copy()` completely separates everything, but now I understand that nested objects can still be shared unless `deepcopy()` is used.

Another important thing I learned is that functions can modify mutable objects directly because Python passes references to the same object. That explains a lot of hidden bugs that can happen in backend systems.

What I’m starting to realize is that this class is not just teaching me Python syntax. It’s teaching me how Python actually behaves internally and how engineers think about memory, objects, and state management.

The biggest mindset shift for me today was this:

Variables do not truly store values directly.
They reference objects in memory.

That one concept connects to:
- mutable bugs
- backend systems
- APIs
- async systems
- AI systems later on

Today genuinely felt like the beginning of thinking more deeply like an engineer instead of just someone writing Python code.

#############################################################

# May 19, 2026 — Day 2

Today’s class honestly stretched my brain more than yesterday’s class.

At first, decorators felt very confusing because there were multiple functions inside other functions, wrappers, returns, and execution flow happening at different stages. I kept mixing up which function was running first.

But as the explanations continued, I slowly started understanding that decorators are basically functions wrapping other functions with extra behavior.

One of the biggest realizations for me today was understanding that decorators are not magic. Python is actually wrapping functions internally.

Closures were also very interesting today. It was difficult at first understanding how a function could still remember variables after the outer function had already finished running, but I’m beginning to understand how closures carry remembered data.

Another important thing I learned is that functions in Python are real objects.

This means:
- functions can be passed around
- stored inside variables
- returned from other functions
- wrapped dynamically

That was a major mindset shift for me.

The *args and **kwargs part also helped me understand how professional decorators are made flexible enough to work with different functions and arguments.

What I’m starting to realize now is that we are no longer just learning Python syntax.

We are learning:
- framework engineering
- reusable architecture patterns
- middleware behavior
- how modern backend systems internally work

Today genuinely felt like I was beginning to understand how Python frameworks are engineered behind the scenes.

##############################################################

# May 20, 2026 — Day 3

Today’s class was honestly one of the most interesting classes so far because I started understanding how scalable systems think about memory and data processing.

At first, iterators felt simple because it looked similar to loops we already learned before, but as the explanations continued, I realized that Python loops are secretly using iterators internally.

That honestly changed the way I look at for loops now.

One major thing I learned today is that iterators keep track of their current position internally and next() keeps moving through items one-by-one until Python raises StopIteration.

Generators were definitely the biggest topic today.

At first, I was still mixing up yield and return, but I finally started understanding that return completely ends a function while yield pauses the function temporarily and later continues exactly where it stopped.

That pause-and-resume behavior was the biggest mindset shift for me today.

I also started understanding why generators are so important in real engineering systems.

Generators help systems avoid loading huge amounts of data into memory at once.

Instead, they process data gradually:
- one item at a time
- pause
- continue
- pause
- continue

This connects directly to:
- streaming systems
- large-file processing
- AI pipelines
- live APIs
- scalable backend systems

Another thing I realized today is that generators are actually a special type of iterator.

That was another important connection for me.

Today genuinely made me feel like I was beginning to understand how scalable systems think about memory efficiency and large data processing internally.

######################################################

# May 21, 2026 — Day 4

Today’s class honestly changed the way I think about backend systems completely.

At first, asynchronous programming looked confusing because I kept thinking async automatically meant everything was running at the exact same time.

But as the explanations continued, I finally started understanding that concurrency is more about efficiently switching between waiting tasks instead of blocking the whole system.

One of the biggest realizations for me today was understanding the difference between blocking and non-blocking operations.

Functions like time.sleep() completely block the program, while await only pauses the current coroutine and allows other tasks to continue running.

That was a huge mindset shift for me.

Another major realization was understanding that async functions are not normal functions. They create coroutine objects and need the event loop to manage them.

The event loop was honestly one of the hardest concepts today, but I’m beginning to understand that it acts like a traffic controller for asynchronous tasks.

It keeps track of:
- waiting tasks
- paused tasks
- resumed tasks
- scheduling operations

I also finally understood why FastAPI is considered fast.

Instead of making requests wait one-by-one sequentially, FastAPI uses asynchronous concurrency to efficiently manage waiting operations and reduce latency.

Today genuinely made me feel like I was beginning to understand how scalable backend systems internally work behind the scenes.

This was honestly one of the most important backend engineering classes so far.

####################################################

# May 22, 2026 — Day 5

Today’s class felt very different from the previous classes because it focused more on engineering thinking and systems reasoning instead of only writing Python code.

This week really changed the way I’m beginning to see backend engineering.

At first, I used to think backend engineering was mainly about writing APIs and making code work. But now I’m starting to realize that real backend engineering involves understanding how systems behave internally.

We reviewed concepts like:

- generators
- async programming
- decorators
- event loops
- mutability
- scalability
- backend reliability

One thing I’m beginning to understand deeply is that concepts in Python are not just “Python topics.” They are connected to real production systems.

For example:

- generators connect to memory efficiency and scalability
- async programming connects to performance and non-blocking systems
- decorators connect to clean backend architecture
- mutability connects to backend reliability and debugging

I also realized that production systems can fail because of:

- memory issues
- blocking operations
- bad architecture decisions
- shared mutable state
- scalability problems

Another important realization is that I’m slowly beginning to think more like an engineer instead of only focusing on syntax.

I’m now paying more attention to:

- system behavior
- backend performance
- scalability
- debugging mindset
- architecture thinking

This week was deeper than I expected, and I can already feel my engineering mindset gradually changing.

#######################################################

# May 25, 2026 — Day 6

Today was the beginning of Week 2, and the focus shifted more into writing Python like a professional backend engineer instead of only learning how Python works internally.

Today’s class was mainly about type hinting and professional function design.

At first, type hints looked simple, but as the class continued, I started understanding that they are very important in backend engineering because they help systems become more predictable and easier to maintain.

I learned that backend engineers use type hints to clearly define:

- what data enters a function
- what data should return from a function
- how backend systems are expected to behave

One important thing I realized is that professional backend code is not only written for computers. It is also written for engineers, teammates, debugging, maintenance, and scalability.

We also discussed why predictable outputs are important in APIs and backend systems because wrong return types can create bugs and production issues.

Another important concept I understood was default values in functions. For example:

```python
is_paid: bool = False
```

This helps backend systems behave safely even when some parameters are not passed into the function.

I also learned why precise typing matters, especially when using things like:

```python
List[int]
```

instead of just normal lists.

This helps engineers know exactly what kind of data is expected inside the system.

Today’s class made me realize more deeply that backend engineering is not just about writing working code. It is also about building readable, scalable, predictable, and production-safe systems.

I’m beginning to understand that clean communication between engineers is also part of professional backend engineering.

#################################################### 

# May 26, 2026 — Day 7

Today’s class was my first real introduction to Object-Oriented Programming from a backend engineering perspective.

Before today, I mostly saw OOP as creating classes and objects, but today I started understanding that backend engineers actually use OOP to model real systems.

We created classes like:

```python
class User
```

and:

```python
class BankAccount
```

This helped me understand that classes act like blueprints for real backend entities.

I also learned more deeply how constructors work using:

```python
__init__()
```

and how objects carry their own internal data and state inside memory.

Another important thing I understood today was methods.

Methods are functions inside classes, but more importantly, they represent behaviors attached directly to objects.

Example:

```python
user1.greet()
```

This feels much cleaner and more scalable than creating random standalone functions everywhere.

One of the biggest realizations I had today was object state.

For example:

```python
self.balance += amount
```

This showed me how backend systems constantly modify object state internally, just like real banking systems update balances after deposits or withdrawals.

We also discussed validation logic inside methods.

Example:

```python
if amount > self.balance:
```

This helped me understand that backend engineers do not trust users completely and that backend systems must always protect themselves from invalid operations.

Today’s class made me realize that backend engineering is really about organizing, modeling, and protecting systems properly.

I’m beginning to understand OOP beyond just syntax.

################################################# 

# May 27, 2026 — Day 8

Today’s class was very interesting because I started understanding inheritance and composition from a real backend engineering perspective.

At first, inheritance looked confusing, but as the explanations continued, I started understanding that inheritance is mainly about reusing shared behavior without rewriting the same code repeatedly.

We created a parent class called:

```python
class User
```

and child classes like:

```python
class Admin(User)
```

and:

```python
class Customer(User)
```

This helped me understand that the child classes inherit behavior from the parent class.

For example, both Admin and Customer could use:

```python
login()
```

without rewriting the login method again.

One major thing I realized today is that inheritance helps backend engineers avoid duplication and build scalable systems with shared behavior.

I also learned about method overriding.

At first, I was confused about it, but later I understood that overriding means a child class can customize inherited behavior.

Example:

```python
class Admin(User):

    def login(self):
```

This means the Admin class can have its own special login behavior, like extra security or OTP verification, while still inheriting from User.

Another major concept today was composition.

This part really changed my understanding of backend architecture.

I learned that composition means systems work together instead of everything inheriting from one giant hierarchy.

Example:

```python
self.notification_service = NotificationService()
```

This means the User class has a NotificationService instead of becoming one.

This helped me understand modular backend architecture and separation of concerns.

One of the biggest realizations I had today is that large backend systems are really about organizing relationships between systems properly.

Today’s class made me understand backend architecture much more deeply than before.

################################################## 

# May 28, 2026 — Day 9

Today’s class was more focused on backend architecture and how large backend systems are properly organized professionally.

One major thing I understood today is that scalable backend engineering is not just about writing APIs or endpoints. It is mostly about how systems are organized internally.

We started learning about separation of concerns.

I already understood this a little from my FastAPI experience because I know backend engineers usually separate files into routers, services, schemas, repositories, and database layers.

But today’s class helped me understand the deeper engineering reason behind that architecture style.

I learned that repositories mainly handle database operations while services handle business logic and workflows.

One important realization I had today is that large backend systems cannot survive if everything is written inside one giant main.py file.

That would become:
- difficult to debug
- stressful to maintain
- dangerous in production
- impossible to scale with teams

Today’s class also connected very well with the previous class on composition.

I learned that composition and separation of concerns work together because modular systems can collaborate safely without becoming tightly connected.

We also discussed tight coupling and loose coupling.

At first, I honestly did not understand the explanation fully, but later the restaurant analogy made everything much clearer.

I now understand that tightly coupled systems are dangerous because changing one system can break multiple other systems.

Loose coupling allows systems to work independently while still collaborating together safely.

One major concept I learned today was dependency injection.

Instead of one system creating another system internally, engineers can inject dependencies into systems so they become easier to replace, test, and maintain later.

Today’s class really changed how I see backend engineering architecture.

I’m beginning to understand that professional backend engineering is mostly about organizing systems properly, not just writing random code.

################################################## 

# May 29, 2026 — Day 10

Today was not focused on learning a completely new concept. Instead, it was an engineering review day where I connected many of the concepts I have learned over the past two weeks.

One thing I noticed today is that backend engineering is becoming less about individual pieces of code and more about understanding how systems work together.

We reviewed services, repositories, composition, separation of concerns, dependency injection, and async thinking.

I worked through several architecture scenarios and practiced identifying which layer should handle each responsibility.

One of the most useful exercises today was breaking down a business workflow into routers, services, and repositories.

I learned that routers mainly receive requests and return responses, repositories handle storage and database operations, while services coordinate business workflows.

Another important realization was understanding how composition allows multiple systems to work together without becoming tightly connected.

We also discussed how these backend concepts will eventually connect to AI systems.

A major breakthrough for me today was realizing that many future AI systems will still follow the same architectural patterns I am learning now.

Even though the technologies may change, the engineering thinking remains the same.

Today's review helped me see the bigger picture and how all the concepts from Week 1 and Week 2 connect together.

#############################################################

## Day 11 — June 1, 2026

Today, I started Week 3 of my AI Engineering journey. The focus of today's lesson was Dependency Injection and understanding how professional backend systems connect different services together.

At first, I was mixing up composition, inheritance, and dependency injection because they all seem related. But as the lesson went on, I started seeing the differences more clearly.

I learned that composition answers the question, "Which systems work together?" For example, a UserService can have an EmailService, NotificationService, or Repository. Different services collaborate to achieve a business goal.

I then learned that dependency injection answers a different question: "How does one service receive another service?" Instead of creating dependencies directly inside a class, professional systems receive those dependencies from outside. This makes systems easier to maintain, test, and scale.

One of the biggest realizations I had today was that hardcoding dependencies can become a nightmare in production systems. If a company decides to switch from one provider to another, engineers may need to change code in many places. With dependency injection, we can simply swap the implementation while keeping the main business logic almost unchanged.

I also understood why dependency injection makes testing easier. During testing, engineers do not always want to send real emails, process real payments, or call real AI APIs. They can inject fake services and focus only on testing the business logic.

Another important realization was that dependency injection is not just a backend concept. The same idea applies to AI systems. An AI service should not depend directly on OpenAI or any single provider. It should be able to work with different model providers such as Claude, Gemini, or local models without major rewrites.

Today's lesson made me realize that production engineering is largely about designing systems for change. Technologies, providers, and business requirements constantly change, and dependency injection is one of the patterns that helps engineers build systems that can adapt without breaking everything.

#############################################################

## Day 12 — June 2, 2026


Today, I learned about Context Managers and why resource management is extremely important in backend engineering.

I started by understanding what resources are in programming. Resources can be things like files, database connections, Redis connections, API connections, sockets, and other objects that a program temporarily uses and must release properly.

One important realization today was that resources are limited. For example, a database can only handle a certain number of active connections at a time. If connections are continuously opened and never closed, they keep accumulating until the database eventually refuses new connections. This can make an application slow, unresponsive, or completely unavailable.

I also learned that Python introduced Context Managers to help engineers safely manage resources. The general idea is:

Acquire Resource
→ Use Resource
→ Release Resource

I learned that the `with` statement automatically handles cleanup for us.

For example:

```python
with open("notes.txt") as file:
    content = file.read()
```

Python automatically opens the file, allows us to use it, and closes it when we leave the block.

I learned that cleanup happens immediately after leaving the `with` block and before the rest of the program continues executing.

I also learned about the two special methods that make Context Managers work:

* `__enter__()`
* `__exit__()`

`__enter__()` is responsible for preparing or acquiring the resource, while `__exit__()` is responsible for cleaning up and releasing the resource.

Another major realization today was that `__exit__()` runs even if an exception occurs inside the `with` block. This guarantees resource cleanup and prevents resource leaks.

I connected this idea to backend engineering and realized that Context Managers are heavily used for:

* database sessions
* transactions
* file handling
* network connections
* locks
* Redis clients
* AI model sessions
* vector database clients

The biggest takeaway from today's class is that professional backend systems are designed around safe resource management. Context Managers make systems more reliable because cleanup is guaranteed whether code succeeds or fails.

Mental model from today:

Acquire Resource
→ Use Resource
→ Automatic Cleanup

And:

`__exit__()` always runs.

#############################################################

## Day 13 — June 3, 2026

### Error Handling and Custom Exceptions

Today, I learned about error handling and why professional backend systems are designed around failure.

I realized that production systems should never assume that everything will always work correctly. Users can provide invalid inputs, databases can become unavailable, external APIs can fail, payment providers can go down, and AI services can become unreachable.

One of the biggest lessons today was understanding the complete exception-handling flow in Python.

I learned:

* `try` is where Python attempts risky code.
* `except` runs only when an exception occurs.
* `else` runs only if the try block succeeds.
* `finally` always runs and is commonly used for cleanup operations like closing database connections and releasing resources.
* `raise` allows engineers to intentionally create exceptions when business rules are violated.
* custom exceptions make large applications easier to understand and maintain.

I also realized that exception handling is not really about preventing applications from crashing. It is about controlling failures and responding to them safely.

Another major lesson today was learning that different layers in a backend system have different responsibilities when failures occur.

### Router

* validates incoming requests
* checks invalid formats
* checks missing fields
* checks incorrect data types

### Service

* handles business rules
* orchestrates workflows
* decides how failures should be handled
* commonly raises business-related exceptions

### Repository

* communicates with the database
* performs queries and persistence operations
* usually notices database-related failures first

The biggest realization today was learning to ask three questions whenever something goes wrong:

Who noticed the problem first?

Who should decide what to do?

What should the user receive?

I practiced this reasoning using examples like user registration, insufficient account balances, payment failures, and database connection problems.

I also learned that professional systems use meaningful exceptions instead of generic ones. Examples include:

* UserAlreadyExistsError
* InsufficientBalanceError
* PaymentProviderError

These custom exceptions make systems easier to debug and easier for other engineers to understand.

Today's lesson felt less like learning Python syntax and more like learning how engineers think when designing reliable systems. I am starting to understand that production engineering is not about avoiding failures completely. It is about designing systems that fail safely, recover gracefully, and continue serving users.

### Mental Model from Today

```text
Failure
↓
Detect Problem
↓
Handle Problem
↓
Return Meaningful Response
↓
Continue Serving Users
```

####################################################### 

## Day 14 — June 4, 2026

### Logging and Observability Foundations

Today, I learned why professional systems rely heavily on logging and why logs are considered one of the most important tools in production engineering.

I learned that logs are records of events happening inside an application. They help engineers understand what the application was doing before a success or failure occurred.

One of my biggest realizations today was that logs are similar to the black box recorder inside an airplane. When something goes wrong, engineers use logs to investigate what happened instead of guessing.

I learned that good logs should answer questions such as:

* What happened?
* Where did it happen?
* When did it happen?
* Was the operation successful?
* Did something fail?

I also learned that not everything should be logged. Sensitive information like passwords, secret keys, tokens, and credit card numbers should never appear inside logs.

Another important lesson today was understanding logging levels.

INFO:
Used for normal application activities.

WARNING:
Used for unusual situations that do not stop the system.

ERROR:
Used when something fails and prevents normal operation.

I also connected today's lesson with our backend architecture.

Router
↓
Service
↓
Repository
↓
Database

I learned that logs can help engineers quickly determine where a failure happened. For example, if a database connection fails, the repository layer usually notices it first and logs the failure as an ERROR.

Another major realization today was understanding the relationship between logs and exceptions.

Exceptions control failures.

Logs explain failures.

Together, they allow applications to fail safely, communicate meaningful responses to users, and continue serving other requests.

Today's lesson felt less like learning Python syntax and more like learning how engineers observe and investigate systems in production.

Mental model from today:

Request
↓
Application Performs Work
↓
Log Important Events
↓
Failures Become Visible
↓
Investigate
↓
Improve Reliability

##################################################   

## Day 15 — June 5, 2026

### Week 3 Engineering Review and Production Systems Thinking

Today was our Week 3 review, and it helped me connect all the concepts I learned throughout the week into one complete backend workflow.

Instead of learning each topic separately, I now understand how they work together inside a real production backend application.

One of the biggest realizations I had this week is that production systems are built with the expectation that failures will happen. The goal is not to prevent every failure, but to detect failures quickly, handle them safely, and allow the application to continue serving users whenever possible.

We reviewed all the major topics from this week:

* Dependency Injection
* Context Managers
* Exception Handling
* Custom Exceptions
* Logging and Observability

I now understand that dependency injection helps reduce coupling by allowing services to receive their dependencies instead of creating them themselves. This makes applications easier to test, maintain, and scale.

I also learned that context managers automatically clean up resources such as database connections and files, even when exceptions occur. This prevents resource leaks and makes production systems much more reliable.

Another important lesson this week was understanding how exceptions work in professional systems. Exceptions are not meant to crash an application. They provide a controlled way of handling failures and returning meaningful responses to users.

Custom exceptions made even more sense after today's review. Instead of using generic exceptions everywhere, professional applications create exceptions that clearly describe what went wrong, making debugging and maintenance much easier.

We also reviewed logging and observability. I learned that logs are written for engineers, not for users. Logs help engineers understand what happened inside an application, while users should receive simple and friendly responses instead of internal error messages.

One of my favorite discussions today was about Redis. Even though I have not learned Redis yet, I learned an important production engineering principle. Not every component failure should stop the entire application. If a cache becomes unavailable but the database is still working, the application should continue operating without the cache whenever possible. This introduced me to the idea of graceful degradation, where systems continue providing service with reduced functionality instead of failing completely.

The biggest mindset shift this week is that I am beginning to think less about writing Python code and more about designing reliable backend systems. Instead of asking, "How do I write this function?", I am starting to ask questions like:

* Which layer should handle this responsibility?
* Where should this failure be detected?
* What should be logged?
* Should the application continue or stop?
* What response should the user receive?

These are the kinds of questions professional backend engineers ask when designing production systems.

### Week 3 Mental Model

```text
User Request
        │
        ▼
Router
        │
        ▼
Dependency Injection
        │
        ▼
Service
        │
        ▼
Repository
        │
        ▼
Context Manager Opens Resources
        │
        ▼
Database

        │
        ▼
If Success
        │
        ▼
Log INFO
        │
        ▼
Return Success

───────────────

If Failure
        │
        ▼
Log ERROR
        │
        ▼
Raise Custom Exception
        │
        ▼
Return Friendly Response
        │
        ▼
Context Manager Cleans Resources
```

This week felt like a major step forward because I can now see how multiple engineering concepts fit together to build reliable, scalable, and production-ready backend systems. This gives me much more confidence that I am progressing toward becoming an AI systems engineer rather than simply learning isolated Python features.

##################################################  

## Day 16 — June 8, 2026

### Testing Mindset and Engineering Thinking

Today marked the beginning of Week 4, and instead of jumping straight into using a testing framework, I learned why testing exists in the first place.

One thing I appreciated about today's class is that we focused on developing the mindset of a tester before learning any new tools. It reminded me that understanding why something exists is more important than memorizing how to use it.

I learned that software engineering is not just about writing code. Professional engineers are responsible for proving that their code works correctly before it reaches users.

We discussed the difference between manual testing and automated testing. Manual testing is useful for small checks, but it becomes inefficient and repetitive as applications grow. Automated testing allows the computer to verify software behavior every time the code changes.

Another important concept I learned today was the difference between a happy path and edge cases.

The happy path represents normal user behavior where everything works as expected.

Edge cases represent unusual situations that could expose hidden bugs, such as:

* empty input fields
* invalid email formats
* weak passwords
* negative values
* zero values
* amounts larger than the available balance

One of the biggest mindset shifts today was learning that testers think differently from programmers.

A programmer often asks:

"Does my code work?"

A tester asks:

"What inputs could cause this code to fail?"

I also learned that every test case should clearly define both the input and the expected output. This makes tests easier to understand, repeat, and automate later using tools like pytest.

Today's lesson connected directly to backend engineering because APIs must be tested against both valid and invalid requests to ensure they behave safely under different conditions.

I can already see how today's mindset will prepare me for writing real automated tests in the coming days.

### Mental Model

Write Code
↓
Think Like a Tester
↓
Design Test Cases
↓
Verify Behavior
↓
Build Reliable Software

#################################################  

## Day 17 — June 9, 2026

### Introduction to pytest and Automated Testing

Today was one of the biggest milestones in my backend engineering journey so far because I installed and used my first professional testing framework: pytest.

Before installing anything, I learned why Python projects use virtual environments. Instead of simply following commands, I understood that virtual environments isolate project dependencies so that each project has its own independent Python environment.

I created my first virtual environment using Python's built-in venv module and activated it successfully. After that, I verified that my project was actually using the Python interpreter inside the virtual environment instead of the global Python installation. This helped me understand that professional engineers verify their environments rather than assuming everything is configured correctly.

Next, I installed pytest using pip. I also learned that installing one package often installs several additional packages known as dependencies. Running `pip list` showed me every package currently installed inside my virtual environment, helping me see how package management works in real projects.

The most exciting part of today's lesson was writing my first automated test.

Instead of printing values manually, I learned how to use the `assert` statement to describe what I expect the code to return. I also learned that pytest automatically discovers functions whose names begin with `test_`, executes them, and reports whether they pass or fail.

Running pytest for the first time and seeing:

`1 passed`

felt like a major achievement. It showed me how professional engineers build confidence in their software by allowing the computer to verify behavior automatically.

One mindset shift I had today was realizing that software engineering is not only about writing code. It is also about building reliable systems that can prove they still work after changes are made.

Today's lesson connected directly to backend engineering because every production API should eventually have automated tests protecting its business logic and preventing regressions.

### Mental Model

Create Environment
↓
Install Dependencies
↓
Write Code
↓
Write Tests
↓
Run pytest
↓
Verify Behavior
↓
Deploy With Confidence



