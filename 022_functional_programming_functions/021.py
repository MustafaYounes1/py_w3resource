"""

Write a Python program that invokes a function after a specified period of time.
    You should write a function that takes in as arguments:
        the function to be delayed with its arguments
        the amount of delay in seconds

def greeting(n: str) -> str:
    return f"Hello {n}!"

print(delay(greeting, 5, "Mustafa"))
// The program should sleep for 5 seconds and then print the following //
Hello Mustafa!

"""

import time
from typing import Callable


def delay(func: Callable[..., ...], t: float, *args) -> ...:
    time.sleep(t)
    return func(*args)


def greeting(n: str) -> str:
    return f"Hello {n}!"


def main():
    print(delay(greeting, 5, "Mustafa"))


if __name__ == "__main__":
    main()
