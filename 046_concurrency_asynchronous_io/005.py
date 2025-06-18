"""

Write a Python program that runs multiple asynchronous tasks concurrently using asyncio.gather() and measures the
time taken.
    Task1: sleep 4 seconds
    Task2: sleep 1 seconds
    Task3: sleep 2 seconds

"""

import asyncio
import logging
import time


logging.basicConfig(
    format="%(asctime)s %(message)s",
    datefmt="%H:%M:%S",
    level=logging.INFO
)


async def func(down_time: int, name: str) -> None:
    logging.info(f"{name} started")
    await asyncio.sleep(down_time)
    logging.info(f"{name} finished")


async def main():
    s = time.perf_counter()

    await asyncio.gather(
        asyncio.create_task(func(4, "Task1")),
        asyncio.create_task(func(1, "Task2")),
        asyncio.create_task(func(2, "Task3")),
    )

    logging.debug(f"Main task elapsed for {time.perf_counter() - s:.3f} sec")


if __name__ == "__main__":
    asyncio.run(main())
