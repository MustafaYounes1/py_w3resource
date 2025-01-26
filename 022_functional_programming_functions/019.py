"""

Write a Python program to access a function inside a function.
    The first function should take an integer as an argument
    The second function should:
        take the same argument
        add 1 to the argument passed to first function
        return summation of both arguments

Use closures:
    Python closure is a nested function that allows us to access variables of the outer function even after the outer
    function is closed.

closure = create_closure(4)

print(closure(5))   =>  10
print(closure(3))   =>  8

"""

from typing import Callable


def create_closure(a: int) -> Callable[[int], int]:
    def closure(b: int) -> int:
        return a + 1 + b
    return closure


def main():
    closure = create_closure(4)
    print(closure(5))
    print(closure(3))


if __name__ == "__main__":
    main()
