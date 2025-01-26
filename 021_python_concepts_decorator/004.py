"""

Write a Python program that
    implements a decorator to cache the result of a function that calculates the product of a list of numbers.
        Note: the cache should have a maxsize that must not get exceeded (FIFO)
    implements a decorator to benchmark the calls product of huge lists


// The cache max size is 2 //

data = [
    [random.randint(1, 1000) for _ in range(200_000)],
    [random.randint(1, 1000) for _ in range(200_000)],
    [random.randint(1, 1000) for _ in range(200_000)]
]

multiply(data[0])       the cache holds the res of: [data[0]]
multiply(data[1])       the cache holds the res of: [data[0], data[1]]
multiply(data[0])       the cache holds the res of: [data[0], data[1]]      (Retrieve the result from the cache)
multiply(data[2])       the cache holds the res of: [data[1], data[2]]
multiply(data[0])       the cache holds the res of: [data[2], data[0]]
multiply(data[1])       the cache holds the res of: [data[0], data[1]]
multiply(data[1])       the cache holds the res of: [data[0], data[1]]      (Retrieve the result from the cache)

took 6.019 sec
took 8.125 sec
multiply was already executed on the given args
took 0.042 sec
took 8.228 sec
took 6.370 sec
took 9.496 sec
multiply was already executed on the given args
took 0.040 sec

"""

from collections import OrderedDict
from functools import reduce
from operator import mul
import random
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


def cache(max_size: int) -> Callable[..., ...]:
    """Cache the result of a function execution"""
    cached_calls: OrderedDict[tuple[int | float | str, ...], ...] = OrderedDict()

    def outer(func: Callable[..., ...]) -> Callable[..., ...]:

        def inner(*args, **kwargs) -> ...:
            call_key = func_args_to_key(list(args) + list(kwargs.values()))
            if call_key in cached_calls:
                print(f"{func.__name__} was already executed on the given args")
                return cached_calls[call_key]

            res = func(*args, **kwargs)
            cached_calls[call_key] = res
            cached_calls.move_to_end(call_key, last=True)

            if len(cached_calls) > max_size:
                cached_calls.popitem(last=False)

            return res

        return inner

    return outer


def benchmark(func: Callable[..., ...]) -> Callable[..., ...]:
    """Benchmark the time of a function execution"""
    def wrapper(*args, **kwargs) -> ...:
        s = time.time()
        res = func(*args, **kwargs)
        print(f"took {time.time() - s:.3f} sec")
        return res
    return wrapper


@benchmark
@cache(max_size=2)
def multiply(iterable: Iterable[int | float]) -> int | float:
    """Multiply the items in an iterable of ints or floats"""
    return reduce(mul, iterable)


def main():
    random.seed(0)

    data = [
        [random.randint(1, 1000) for _ in range(200_000)],
        [random.randint(1, 1000) for _ in range(200_000)],
        [random.randint(1, 1000) for _ in range(200_000)]
    ]

    multiply(data[0])
    multiply(data[1])
    multiply(data[0])
    multiply(data[2])
    multiply(data[0])
    multiply(data[1])
    multiply(data[1])


if __name__ == "__main__":
    main()
