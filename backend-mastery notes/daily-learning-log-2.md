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

#################################################  

## Day 18 — June 10, 2026

### Reading pytest Failure Reports and Multiple Tests

Today's lesson completely changed the way I look at failed tests.

Yesterday, I celebrated seeing my first passing test. Today, I intentionally made a test fail so I could learn how professional engineers read pytest failure reports.

Instead of being overwhelmed by the red output, I learned to treat it like a debugging guide. I now know how to identify which test failed, the exact line that caused the failure, the actual value returned by the function, the expected value defined by the test, and why pytest raises an AssertionError.

One of the biggest lessons today was understanding that a failed test does not automatically mean the application is wrong. Sometimes the code has a bug, but other times the test itself has the wrong expectation. From now on, whenever a test fails, I should first ask whether the application is incorrect or whether my test is incorrect.

I also learned how pytest discovers tests automatically. It searches for files and functions that follow the `test_` naming convention and executes every discovered test. If one test fails, pytest usually continues running the remaining tests before showing a summary of all passing and failing tests.

Another important mindset shift came when discussing withdrawal examples. I realized that testing is not only about calculating numbers. Before calculating a result, I should first ask whether the requested operation is even valid according to the business rules. Invalid inputs should be rejected rather than processed.

Today's class helped me move beyond simply writing tests. I began learning how to investigate failures, reason about expectations, and think more like a backend engineer responsible for maintaining reliable software.

### Mental Model

Run Tests
↓
Read Failure Report
↓
Compare Actual vs Expected
↓
Identify the Root Cause
↓
Fix the Code or the Test
↓
Run Tests Again  

#################################################  

## Day 19 — June 11, 2026

### Parameterized Testing and the DRY Principle

Today's lesson helped me understand one of the most practical features of pytest: parameterized testing.

At first, I thought it was simply another pytest feature, but I realized it is actually an application of a much bigger software engineering principle: DRY (Don't Repeat Yourself).

I learned that many tests use exactly the same logic and differ only in their input values and expected outputs. Instead of creating many nearly identical test functions, pytest allows one reusable test to execute automatically with multiple datasets.

One important realization today was that parameterized testing is not just about writing less code. It is about improving maintainability. If the testing logic ever changes, I only need to update one test function instead of many duplicated ones.

I also learned to think beyond small classroom examples. I asked what would happen if a project contained thousands of test cases instead of only five. This helped me understand that pytest is designed for large production systems and provides summarized output rather than overwhelming developers with thousands of individual test results.

Another important lesson was recognizing that professional engineers constantly look for patterns they can reuse. Before writing new code, they ask whether the logic already exists and whether duplication can be avoided.

Today's lesson reinforced that software engineering is not only about making programs work. It is also about designing solutions that remain clean, scalable, and maintainable as projects grow.

### Mental Model

One Test
↓

Many Datasets
↓

Many Independent Test Executions
↓

Less Duplication
↓

Easier Maintenance
↓

Scalable Testing

#################################################  

## Day 20 — June 12, 2026

### Engineering Review – Testing and Debugging Mindset

Today was a review day, and instead of learning a completely new topic, I spent time connecting everything I learned throughout Week 4.

Looking back, I realized that this week was not really about learning pytest syntax. It was about learning why professional backend teams rely on automated testing and how testing supports confident software development.

One of the biggest lessons today was understanding that a failing test is not something to fear. A failed test is valuable information that helps engineers locate problems before software reaches production.

I also reflected on parameterized testing and the DRY principle. I now understand that professional engineers constantly look for repeated patterns and replace duplicated logic with reusable solutions. This idea applies not only to testing but also to backend architecture and software design in general.

Another important lesson today was strengthening my debugging mindset. Instead of immediately assuming where the bug is, I learned to begin with questions:

- What changed?
- What depends on that change?
- Is there shared code?
- What evidence supports my hypothesis?

This way of thinking encourages investigation before modification and reduces the risk of introducing new bugs.

One of the discussions that stood out to me today was thinking about what happens when an unrelated test suddenly fails after modifying another part of the system. I realized that this does not automatically mean the failed feature is broken. It may indicate shared dependencies or unintended side effects, which require proper root cause analysis.

By the end of today's class, I felt that I was no longer learning isolated Python concepts. I was beginning to connect testing, debugging, architecture, and systems thinking into one complete engineering workflow.

### Mental Model

Change Code

↓

Run Automated Tests

↓

Analyze Results

↓

Investigate Root Cause

↓

Fix the Problem

↓

Run Tests Again

↓

Deploy With Confidence

#################################################  

## Day 21 — June 15, 2026 (Monday)

Today I started Week 5, which focuses on professional testing and code quality.

The biggest lesson today was understanding pytest fixtures. At first, I thought a fixture was just another function, but I learned that pytest treats it specially. It automatically runs the fixture, receives the returned object, and injects it into the test function without me calling it directly.

One of the most important concepts I learned today was **test isolation**. I initially thought pytest might create one object and share it across all tests, but I discovered that it creates a fresh object for each test by default. This prevents one test from accidentally affecting another, making automated tests more reliable and predictable.

Another interesting discovery was pytest's test discovery system. My first fixture file wasn't executed because it didn't begin with `test_`. After renaming the file to `test_fixture_experiments.py`, pytest immediately discovered and executed both tests successfully.

I also learned that pytest captures print statements by default. Running `pytest` hid my `print()` output, while running `pytest -s` displayed the fixture execution, allowing me to clearly see that the fixture was executed before each test.

Today's lesson also helped me connect several topics from previous weeks. I realized that fixtures are another form of dependency injection, but instead of injecting dependencies into an application, pytest injects prepared objects into tests. This showed me how different backend engineering concepts are connected rather than being isolated topics.

Overall, today's class strengthened my understanding of automated testing, backend maintainability, and professional engineering practices. I'm beginning to see how testing frameworks are designed to support large, scalable projects with thousands of tests.

#################################################  

## Day 22 — June 16, 2026 (Tuesday)

Today I continued Week 5 by learning about fixture scopes in pytest. Yesterday I learned that pytest creates a fresh fixture for every test, but today I discovered that this default behavior is not always the most efficient approach for large backend projects.

I learned that pytest provides different fixture scopes, including function, class, module, and session. Each scope controls how often a fixture is created and reused. The lesson focused on understanding that fixture scope is an engineering decision rather than something to memorize.

One of the biggest ideas today was the trade-off between performance and test isolation. Smaller scopes, such as function scope, provide better isolation because each test receives a fresh object. Larger scopes, such as module or session scope, improve performance by sharing resources, but they also increase the risk of shared mutable state causing tests to affect one another.

I also connected today's lesson with concepts from previous weeks. The discussion about shared dictionaries reminded me of Python mutable objects from Week 1, while fixture injection continued reinforcing dependency injection concepts from Week 3. This showed me that many backend engineering ideas are interconnected rather than isolated topics.

Although fixture scopes are not the most exciting topic, I now understand why they matter in production systems. Large engineering teams must constantly balance correctness, maintainability, and performance when designing automated test suites. This lesson strengthened my understanding of how professional backend engineers make those decisions.

################################################# 

## Day 23 — June 17, 2026 (Wednesday)

Today's lesson focused on one of the most practical pytest concepts so far: yield fixtures. I learned that a fixture can perform both setup and cleanup automatically by using the `yield` keyword instead of `return`.

One of the biggest realizations today was that yield fixtures are very similar to Python context managers that I learned during Week 3. Both approaches manage the complete lifecycle of a resource by preparing it before use and cleaning it up automatically afterward.

Through several experiments, I observed the difference between function scope and module scope. With the default function scope, pytest created a new fixture for every test, performed the setup, ran the test, and immediately executed the cleanup. After changing the fixture to module scope, I saw that pytest created the fixture only once, shared it between both tests, and delayed the cleanup until every test in the module had completed.

I also completed my first production-style testing experiment by replacing a simple dictionary fixture with a simulated database connection. This helped me understand how FastAPI applications manage database sessions during automated testing. The pattern of connecting before the test, yielding the resource, and closing it afterward now makes much more sense.

Today's lesson also reinforced that automated testing is not just about assertions. It is equally important to think about the lifecycle of resources, proper cleanup, performance, and preventing resource leaks. I can now see how pytest fixtures, dependency injection, and context managers all work together to support clean and maintainable backend systems.

################################################# 

## Day 24 — June 18, 2026 (Thursday)

Today's lesson introduced mocking, one of the most important concepts in professional backend testing. I learned that unit tests should focus on verifying my application's logic rather than depending on external services.

Using `MagicMock`, I created a fake payment gateway and configured it to return different responses without making any real API calls. This allowed me to test both successful and failed payment scenarios using the same business logic.

One important realization today was that the business logic did not need to change. Only the mocked response changed, making it possible to verify multiple scenarios safely and quickly.

During the lesson, I also encountered a `NameError` because I created a new test file without importing `MagicMock`. By reading the traceback carefully, I identified the missing import and fixed the issue. This reinforced the importance of debugging methodically instead of guessing.

I now understand that mocking is essential when testing integrations with payment gateways, email services, databases, and AI APIs because it keeps tests fast, predictable, and independent of external systems.

################################################# 

## Day 25 — June 19, 2026 (Friday)

Today marked the completion of Week 5: Professional Testing and Code Quality. Rather than introducing new concepts, today's class focused on connecting everything learned throughout the week into a complete backend testing workflow.

One of the biggest lessons today was understanding how the different testing tools complement one another. Pytest provides the testing framework, fixtures manage reusable setup, yield fixtures handle resource cleanup, fixture scopes control resource lifecycles, and mocking isolates external dependencies from the application's business logic.

I also reinforced why backend services typically return structured dictionaries instead of simple strings. Structured responses allow APIs to communicate additional information such as success status, messages, transaction references, amounts, and other metadata that frontend applications and other services can consume.

During today's review, I practiced reasoning about runtime errors and assertion failures before executing code. I also reviewed common debugging scenarios involving `NameError`, `KeyError`, and `AssertionError`, improving my ability to interpret Python tracebacks and identify root causes efficiently.

Completing Week 5 has given me a much stronger understanding of professional testing practices. I now appreciate that effective testing is not only about writing assertions but also about designing code that is maintainable, testable, and independent of external systems.

This concludes Week 5 of my Backend Engineering Mastery roadmap and prepares me to begin Week 6, where I will focus on PostgreSQL, SQLAlchemy, and production database engineering.



