"""

Write a Python program to create a decorator to convert the return value of a function to a specified data type.

@cast_return_to(float)
def add_integers(a: int, b: int) -> int:
    return a + b

res = add_integers(1, 2)

>   3.0 is of type: <class 'float'>

"""

from typing import Callable, Type


def cast_return_to(out_type: Type) -> Callable[..., ...]:
    def outer(func: Callable[..., ...]) -> Callable[..., ...]:
        def inner(*args, **kwargs) -> ...:
            res = func(*args, **kwargs)
            return out_type(res)
        return inner
    return outer


@cast_return_to(float)
def add_integers(a: int, b: int) -> int:
    return a + b


def main():
    res = add_integers(1, 2)
    print(f"{res} is of type: {type(res)}")


if __name__ == "__main__":
    main()
