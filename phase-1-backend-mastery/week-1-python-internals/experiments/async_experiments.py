# ==========================================
# SYNCHRONOUS EXECUTION
# ==========================================

""" import time


def task_one():

    print("Starting Task One")

    time.sleep(3)

    print("Finished Task One")


def task_two():

    print("Starting Task Two")

    time.sleep(2)

    print("Finished Task Two")


task_one()
task_two() """

# ==========================================
# ASYNCHRONOUS EXECUTION
# ==========================================

""" import asyncio


async def task_one():

    print("Starting Task One")

    await asyncio.sleep(3)

    print("Finished Task One")


async def task_two():

    print("Starting Task Two")

    await asyncio.sleep(2)

    print("Finished Task Two")


async def main():

    await task_one()
    await task_two()


asyncio.run(main()) """

# ==========================================

""" import asyncio


async def task_one():

    print("Starting Task One")

    await asyncio.sleep(3)

    print("Finished Task One")


async def task_two():

    print("Starting Task Two")

    await asyncio.sleep(2)

    print("Finished Task Two")


async def main():

    await asyncio.gather(
        task_one(),
        task_two()
    )


asyncio.run(main()) """

#################################################

""" import asyncio


async def greet():

    print("Hello")

    await asyncio.sleep(2)

    print("Engineer")


asyncio.run(greet()) """

##################################################

import asyncio


async def fetch_user():

    print("Fetching user data...")

    await asyncio.sleep(3)

    print("User data received")


async def fetch_orders():

    print("Fetching orders...")

    await asyncio.sleep(2)

    print("Orders received")


async def fetch_payments():

    print("Fetching payments...")

    await asyncio.sleep(1)

    print("Payments received")


async def main():

    await asyncio.gather(
        fetch_user(),
        fetch_orders(),
        fetch_payments()
    )


asyncio.run(main())