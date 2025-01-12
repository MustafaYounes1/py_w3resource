"""

Write a Python program to count the number of times a specific element appears in a deque object.

(2, 9, 0, 8, 2, 4, 0, 9, 2, 4, 8, 2, 0, 4, 2, 3, 4, 0)

2   =>      5
4   =>      4

"""

from collections import deque


def main():
    d = deque((2, 9, 0, 8, 2, 4, 0, 9, 2, 4, 8, 2, 0, 4, 2, 3, 4, 0) )
    items = 2, 4

    for i in items:
        print(d.count(i))


if __name__ == "__main__":
    main()
