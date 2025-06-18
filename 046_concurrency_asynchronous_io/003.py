"""

Write a Python program that creates an asyncio event loop and runs a coroutine that prints numbers from 1 to 7 with
a delay of 1 second each.

"""

import asyncio
from typing import AsyncGenerator


async def async_generator() -> AsyncGenerator[int, None]:
    for idx in range(1, 8):
        await asyncio.sleep(1)
        yield idx


async def main():
    async for _ in async_generator():
        print(_)


if __name__ == "__main__":
    asyncio.run(main())
