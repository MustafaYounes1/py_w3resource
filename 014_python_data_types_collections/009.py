"""

Write a Python program to add more elements to a deque object from an iterable object.

The deque should contain (2, 4, 6, 8, 10) at first, then add (12, 14, 16, 18, 20) to the left

[20, 18, 16, 14, 12, 2, 4, 6, 8, 10]

"""

from collections import deque


def main():
    d = deque((2, 4, 6, 8, 10))
    # would add element to the left sequentially: 12 -> 14 -> ..
    d.extendleft((12, 14, 16, 18, 20))
    print(list(d))


if __name__ == "__main__":
    main()
