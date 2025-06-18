"""

Write a Python program that implements a timeout for an asynchronous operation using asyncio.wait_for().

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
    logging.info(f"{name} started")
    await asyncio.sleep(random.randint(10, 15))
    logging.info(f"{name} finished")


async def main():
    try:
        await asyncio.wait_for(func("Task 1"), timeout=random.randint(10, 15))

    except asyncio.TimeoutError:
        logging.debug("Timeout occurred")


if __name__ == "__main__":
    asyncio.run(main())
