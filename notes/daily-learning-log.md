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