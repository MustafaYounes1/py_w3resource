"""

Write a Python program that implements a decorator to validate function arguments based on a given condition.
    The decorator should return the multiplication of a sequence if all of its elements are positive
    Otherwise the decorator should raise an error

print(multiply([1, 2, 3, 5]))
print(multiply([1, 2, -3, 5]))

30
ValueError: The function arguments don't statisfy the specified condition

"""

from functools import reduce
from operator import mul
from typing import Callable, Iterable


def validate_args(condition: Callable[..., bool]) -> Callable[..., ...]:
    def outer(func: Callable[..., ...]) -> Callable[..., ...]:
        def inner(*args, **kwargs) -> ...:
            if condition(*args, **kwargs):
                res = func(*args, **kwargs)
                return res
            else:
                raise ValueError("The function arguments don't statisfy the specified condition")
        return inner
    return outer


@validate_args(lambda iterable: all(_ >= 0 for _ in iterable))
def multiply(iterable: Iterable[int | float]) -> int | float:
    return reduce(mul, iterable)


def main():
    print(multiply([1, 2, 3, 5]))
    print(multiply([1, 2, -3, 5]))


if __name__ == "__main__":
    main()
