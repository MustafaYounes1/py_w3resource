"""

Write a Python program to create an iterator from several iterables in a sequence and display the elements of the
new iterator.

[(10, 20, 30, 40), ('A', 'B', 'C', 'D'), (40, 50, 60, 70, 80, 90)]

10 20 30 40 A B C D 40 50 60 70 80 90

"""

from itertools import chain


def main():
    lst = [(10, 20, 30, 40), ('A', 'B', 'C', 'D'), (40, 50, 60, 70, 80, 90)]
    itr = chain.from_iterable(lst)
    for _ in itr:
        print(_, end=" ")


if __name__ == "__main__":
    main()
