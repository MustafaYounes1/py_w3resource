"""

Write a Python program to generate an infinite cycle of elements from an iterable.
    Print the first 3 cycles

['A', 'B', 'C', 'D']   =>  A B C D A B C D A B C D

"""

from itertools import cycle


def main():
    lst = ['A', 'B', 'C', 'D']
    itr = cycle(lst)
    for _ in range(len(lst) * 3):
        print(next(itr), end=" ")


if __name__ == "__main__":
    main()
