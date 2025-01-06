"""

Write a Python program to change the position of every n-th value to the (n+1)th in a list.

[0, 1, 2, 3, 4, 5]   =>  [1, 0, 3, 2, 5, 4]

"""

from itertools import chain, zip_longest


def main():
    lst = [0, 1, 2, 3, 4, 5]
    print(
        list(
            chain.from_iterable(
                zip_longest(lst[1::2], lst[0::2])
            )
        )
    )


if __name__ == "__main__":
    main()
