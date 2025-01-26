"""

Write a Python program to create a decorator that logs the name + the arguments + the returned value of a function.

@func_logger
def test(*args, **kwargs) -> None:
    ...

test(1, 0, None, name="Mustafa", age=28)

>>      'test' called with the positional args: '(1, 0, None)', and keyword args: '{'name': 'Mustafa', 'age': 28}'
        'test' returned the value: 'None'

"""

from typing import Callable


def func_logger(func: Callable[..., ...]) -> Callable[..., ...]:
    def wrapper(*args, **kwargs) -> ...:
        print(f"'{func.__name__}' called with the positional args: '{args}', and keyword args: '{kwargs}'")
        res = func(*args, **kwargs)
        print(f"'{func.__name__}' returned the value: '{res}'")
        return res
    return wrapper


@func_logger
def test(*args, **kwargs) -> None:
    ...


def main():
    _ = test(1, 0, None, name="Mustafa", age=28)


if __name__ == "__main__":
    main()
