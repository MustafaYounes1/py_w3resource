"""

Write a Python function to sum all the numbers in a list.

[8, 2, 3, 0, 7]     =>  20

"""

from functools import reduce
from operator import add


def sum_list(lst: list[int | float]) -> int | float:
    return reduce(add, lst)


def main():
    print(sum_list([8, 2, 3, 0, 7]))


if __name__ == "__main__":
    main()
