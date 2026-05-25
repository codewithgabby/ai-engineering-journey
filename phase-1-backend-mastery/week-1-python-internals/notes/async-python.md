# Async Python

## Synchronous Execution

Today I learned that synchronous execution means tasks run one after another sequentially.

One task must completely finish before another task starts.

This creates waiting time and can slow down systems badly.

---

## Blocking

One important thing I learned today is the idea of blocking.

Functions like time.sleep() block the entire program temporarily.

While the program is waiting:
- nothing else can run
- everything pauses
- execution becomes inefficient

This helped me understand why normal synchronous systems struggle with scalability.

---

## Async Functions

I learned that async functions are different from normal Python functions.

Using async tells Python that the function can:
- pause temporarily
- resume later
- cooperate with other tasks

This was one of the biggest mindset shifts today.

---

## await

The await keyword pauses only the current coroutine temporarily instead of blocking the entire program.

While one task is waiting:
- other tasks can continue running
- the event loop manages other available work

This is one of the reasons asynchronous systems are much faster and more scalable.

---

## Concurrency

Concurrency was the biggest topic today.

Concurrency allows multiple tasks to make progress efficiently while waiting operations happen in the background.

I learned that concurrency is not exactly “doing everything at the same exact time.”

Instead, it is efficiently switching between waiting tasks.

This was a very important engineering realization for me.

---

## asyncio.gather()

asyncio.gather() allows multiple coroutines to run concurrently.

This was the first time I really understood how systems like FastAPI can process many requests efficiently.

Different tasks can start together and whichever task finishes first responds first.

---

## Event Loop

The event loop is the engine behind asynchronous Python.

The event loop:
- schedules tasks
- pauses tasks
- resumes tasks
- manages waiting operations

Without the event loop, asynchronous Python cannot work.

This honestly helped me understand FastAPI architecture more deeply.

---

## Coroutine Functions

I learned that async functions create coroutine objects.

They are not normal functions.

Python needs the event loop to manage and execute them properly.

This was another important realization today.

---

## Latency

One major backend engineering term I learned today was latency.

Latency is basically delay caused by waiting operations.

Concurrency helps reduce latency because while one task waits, another task can continue running.

---

## FastAPI Connection

Today made me finally start understanding why FastAPI is fast.

Instead of blocking the entire server while waiting:
- the event loop switches between requests
- handles other available tasks
- improves scalability and responsiveness

This was a very important backend engineering connection for me today.