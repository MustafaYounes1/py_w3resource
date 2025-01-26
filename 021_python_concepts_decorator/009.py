"""

Write a Python program that implements a decorator to enforce type checking on the arguments of a function.
    The decorator would check that all args are of the annotated datatype if not it would raise TypeError

@arg_type_check
def f1(x: int, y: int, z: str) -> ...:
    ...


@arg_type_check
def f2(name: str, age: int, salary: float) -> ...:
    ...


f1(1, 1, "s")  # f1 executed successfully
f1(1, 1.0, "s")  # 'y' should be of type: 'int'
f1("1", 1, "s")  # 'x' should be of type: 'int'
f2(age=1, salary=100.25, name="Mike")  # f2 executed successfully
f2(salary=22, name="Mike", age=1)  # 'salary' should be of type: 'float'
f2(salary=1.2, name="Mike", age=[1, 2])  # 'age' should be of type: 'int'

"""

from collections import abc
import inspect
from typing import Callable


def arg_type_check(func: Callable[..., ...]) -> Callable[..., ...]:
    signature = inspect.signature(func)
    params = signature.parameters
    params_names = list(params.keys())

    def wrapper(*args, **kwargs) -> ...:
        for i, arg in enumerate(args):
            if not isinstance(arg, params[params_names[i]].annotation):
                raise TypeError(
                    f"'{params_names[i]}' should be of type: '{params[params_names[i]].annotation.__name__}'"
                )

        for arg_name, arg in kwargs.items():
            if not isinstance(arg, params[arg_name].annotation):
                raise TypeError(f"'{arg_name}' should be of type: '{params[arg_name].annotation.__name__}'")

        res = func(*args, **kwargs)
        print(f"{func.__name__} executed successfully")

        return res

    return wrapper


@arg_type_check
def f1(x: int, y: int, z: str) -> ...:
    ...


@arg_type_check
def f2(name: str, age: int, salary: float) -> ...:
    ...


def main():
    try:
        f1(1, 1, "s")  # f1 executed successfully
        f1(1, 1.0, "s")  # 'y' should be of type: 'int'
        f1("1", 1, "s")  # 'x' should be of type: 'int'
        f2(age=1, salary=100.25, name="Mike")  # f2 executed successfully
        f2(salary=22, name="Mike", age=1)  # 'salary' should be of type: 'float'
        f2(salary=1.2, name="Mike", age=[1, 2])  # 'age' should be of type: 'int'

    except TypeError as e:
        print(e)


if __name__ == "__main__":
    main()
