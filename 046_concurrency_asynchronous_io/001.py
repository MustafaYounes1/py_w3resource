"""

Write a Python program that creates an asynchronous function to print "Python Exercises!" with a two-second delay.

"""

import asyncio


async def async_greeting() -> None:
    await asyncio.sleep(2)
    print("Python Exercises!")


async def main():
    await async_greeting()


if __name__ == "__main__":
    asyncio.run(main())
