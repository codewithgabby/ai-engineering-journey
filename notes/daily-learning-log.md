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

