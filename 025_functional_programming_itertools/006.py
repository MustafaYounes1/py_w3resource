"""

Write a Python program to make an iterator that drops elements from the iterable as long as the elements are negative;
afterward, it returns every element.

[-1, -2, -3, 4, -10, 2, 0, 5, 12]   =>  [4, -10, 2, 0, 5, 12]

"""

from itertools import dropwhile


def main():
    lst = [-1, -2, -3, 4, -10, 2, 0, 5, 12]
    print(list(dropwhile(lambda _: _ < 0, lst)))


if __name__ == "__main__":
    main()
