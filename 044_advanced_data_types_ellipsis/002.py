"""

Write a Python function that takes a function as an argument and calls it with any number of arguments.

"""

from typing import Callable


def do_nothing(*args, **kwargs) -> None:
    ...


def func(f: Callable[..., None], *args: ..., **kwargs: ...) -> None:
    return f(args, kwargs)


def main():
    func(do_nothing, 1, 2, 3, name="do_nothing")


if __name__ == "__main__":
    main()
