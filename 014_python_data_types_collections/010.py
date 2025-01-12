"""

Write a Python program to remove all the elements of a given deque object that has the following vals [1, 3, 5, 7, 9].

deque([])

"""

from collections import deque


def main():
    d = deque([1, 3, 5, 7, 9])
    d.clear()
    print(d)


if __name__ == "__main__":
    main()
