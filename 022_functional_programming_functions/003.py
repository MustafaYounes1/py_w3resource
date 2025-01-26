"""

Write a Python function to multiply all the numbers in a list.

[8, 2, 3, -1, 7]    =>  -336

"""

from functools import reduce
from operator import mul


def mul_list(lst: list[int | float]) -> int | float:
    return reduce(mul, lst)


def main():
    print(mul_list([8, 2, 3, -1, 7]))


if __name__ == "__main__":
    main()
