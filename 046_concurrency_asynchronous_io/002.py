"""

Write a Python program that creates three asynchronous functions and displays their respective names with different
delays (1 second, 2 seconds, and 3 seconds).

"""

import asyncio


async def func(delay: float, name: str) -> None:
    await asyncio.sleep(delay)
    print(f"{name} is done.")


async def main():
    await asyncio.gather(
        asyncio.create_task(func(1, "Coroutine 1")),
        asyncio.create_task(func(2, "Coroutine 2")),
        asyncio.create_task(func(3, "Coroutine 3")),
    )


if __name__ == "__main__":
    asyncio.run(main())
