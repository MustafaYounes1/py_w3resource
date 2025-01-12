"""

Write a Python program to remove duplicate words from a given string. Use the collections module.

Python Exercises Practice Solution Exercises

Python Exercises Practice Solution

"""

from collections import OrderedDict


def main():
    s = "Python Exercises Practice Solution Exercises".split()

    d = OrderedDict(
        {k: None for k in s}
    )

    print(" ".join(d.keys()))


if __name__ == "__main__":
    main()
