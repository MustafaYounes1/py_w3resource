"""

Write a Python program to check if a given number is even or odd using boolean variables.

10  ->  Even
7   ->  Odd

"""

from typing import Literal


def _is_even(n: int) -> bool:
    return n % 2 == 0


def even_or_odd(n: int) -> Literal["Even", "Odd"]:
    assert isinstance(n, int), "expected an integer"

    if _is_even(n):
        return "Even"
    else:
        return "Odd"


def main():
    print(even_or_odd(10))
    print(even_or_odd(7))


if __name__ == "__main__":
    main()
