"""

Write a Python program to create a decorator function to measure the execution time of a function.

@func_benchmark
def test(s: int, e: int) -> int:
    i = 0
    for _ in range(s, e):
        i += 1

    return i

_ = test(0, 100_000_000)

>>      test took 4.833 sec
        Result of the execution: 100,000,000

"""

import time
from typing import Callable


def func_benchmark(func: Callable[..., ...]) -> Callable[..., ...]:
    def wrapper(*args, **kwargs) -> ...:
        s = time.time()
        res = func(*args, **kwargs)
        print(f"{func.__name__} took {time.time() - s:.3f} sec")
        return res
    return wrapper


@func_benchmark
def test(s: int, e: int) -> int:
    i = 0
    for _ in range(s, e):
        i += 1
    return i


def main():
    _ = test(0, 100_000_000)
    print(f"Result of the execution: {_:,d}")


if __name__ == "__main__":
    main()
