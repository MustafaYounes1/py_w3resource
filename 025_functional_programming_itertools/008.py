"""

Write a Python program to split an iterable and generate iterables a specified number of times.

['A', 'B', 'C', 'D']
    ['A', 'B', 'C', 'D']
    ['A', 'B', 'C', 'D']
    ['A', 'B', 'C', 'D']
    ['A', 'B', 'C', 'D']
    ['A', 'B', 'C', 'D']

"""

from itertools import tee


def main():
    lst = ['A', 'B', 'C', 'D']
    iters = tee(lst, 5)
    for _ in iters:
        print(list(_))


if __name__ == "__main__":
    main()
