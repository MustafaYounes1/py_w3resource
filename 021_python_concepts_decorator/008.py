"""

Write a Python program that implements a decorator to handle exceptions raised by a function and provide a default
response. Your decorator should provide a default value for all ArithmeticErrors (e.g. division by zero)

print(divide(1, 2))
print(divide(1, 0))

0.5
An arithmetic error occurred: 'division by zero', returning the default value: 0.0
0.0

"""

from typing import Callable


def arithmetic_error_handler(default_val: int | float) -> Callable[..., ...]:
    def outer(func: Callable[..., ...]) -> Callable[..., ...]:
        def inner(*args, **kwargs) -> ...:
            try:
                return func(*args, **kwargs)
            except ArithmeticError as e:
                print(f"An arithmetic error occurred: '{e}', returning the default value: {default_val}")
                return default_val
        return inner
    return outer


@arithmetic_error_handler(0.0)
def divide(a: int | float, b: int | float) -> float:
    return a / b


def main():
    print(divide(1, 2))
    print(divide(1, 0))


if __name__ == "__main__":
    main()
