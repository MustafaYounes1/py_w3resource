"""

Write a Python program to create an iterator with infinite elements [3, 4, 5, inf] and print the first 5 elements

"""

from itertools import count


def main():
    c = count(start=3, step=1)

    print(next(c))
    print(next(c))
    print(next(c))
    print(next(c))
    print(next(c))


if __name__ == "__main__":
    main()
