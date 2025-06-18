"""

Write a Python program to create a coroutine that simulates a time-consuming task and use asyncio.CancelledError to
handle task cancellation.

"""

import asyncio
import logging
import random


random.seed(44)

logging.basicConfig(
    format="%(asctime)s %(message)s",
    datefmt="%H:%M:%S",
    level=logging.DEBUG
)


async def func(name: str) -> None:
    try:
        logging.info(f"{name} started.")

        # simulate some multistep heavy work
        for _ in range(3):
            await asyncio.sleep(random.randint(1, 5))
            logging.debug(f"{name} finished step {_}")

        logging.info(f"{name} finished.")

    except asyncio.CancelledError:
        logging.info(f"{name} was cancelled.")

    finally:
        logging.info(f"{name} cleaning ups.")


async def main():
    task = asyncio.create_task(func("Task 1"))
    await asyncio.sleep(6)  # allow the above task to start
    task.cancel()
    await task  # await for the cleanups


if __name__ == "__main__":
    asyncio.run(main())
