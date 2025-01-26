"""

Write a Python program that implements a decorator to provide caching with expiration time for a function.
    Implement a function that would calculate the multiplication of an Iterable and return the result
    Cache the returned values for provided arguments and the cache should expire in s seconds


@cache(expiry_time=5)
def multiply(iterable: Iterable) -> int | float:
    return reduce(mul, iterable)


print(multiply([1, 2, 3]))
print(multiply([15, 14, 6, 2, 7]))
print(multiply([1, 2, 3]))
print(multiply([15, 14, 6, 2, 7]))
print("Sleep for 5 second ...")
time.sleep(5)
print(multiply([15, 14, 6, 2, 7]))

6
17640
multiply was already executed on the given args (1, 2, 3)
6
multiply was already executed on the given args (15, 14, 6, 2, 7)
17640
Sleep for 5 second ...
17640

"""

from functools import reduce
from operator import mul
import time
from typing import Callable, Iterable


def func_args_to_key(args: list[...]) -> tuple[int | float | str, ...]:
    """Convert a list of arguments of any type (int, float, str, iterable, iterable of iterables, ...) to a flat
    tuple that holds only flat items of int, float, or str."""
    flattened = []
    for _ in args:
        if isinstance(_, (list, tuple, dict)):
            flattened += func_args_to_key(_)
        elif isinstance(_, (int, float, str)):
            flattened.append(_)
        else:
            raise TypeError("Supported primitive types are: {int, float, str}")
    return tuple(flattened)


def cache(expiry_time: float) -> Callable[..., ...]:
    t = time.time()
    cached_calls: dict[tuple[int | float | str, ...], ...] = {}

    def outer(func: Callable[..., ...]) -> Callable[..., ...]:

        def inner(*args, **kwargs) -> ...:
            nonlocal t, cached_calls

            if time.time() - t >= expiry_time:
                t = time.time()
                cached_calls = {}

            call_key = func_args_to_key(list(args) + list(kwargs.items()))
            if call_key in cached_calls:
                print(f"{func.__name__} was already executed on the given args {call_key}")
                return cached_calls[call_key]

            res = func(*args, **kwargs)
            cached_calls[call_key] = res
            return res

        return inner

    return outer


@cache(expiry_time=5)
def multiply(iterable: Iterable) -> int | float:
    return reduce(mul, iterable)


def main():
    print(multiply([1, 2, 3]))
    print(multiply([15, 14, 6, 2, 7]))
    print(multiply([1, 2, 3]))
    print(multiply([15, 14, 6, 2, 7]))

    print("Sleep for 5 second ...")
    time.sleep(5)

    print(multiply([15, 14, 6, 2, 7]))


if __name__ == "__main__":
    main()
