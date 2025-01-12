"""

Write a Python program to create a deque from an existing iterable object (2, 4, 6) and make the required operations
to let it have the following final items: [2, 2, 4, 6, 8, 10, 12]

"""

from collections import deque


def main():
    t = (2, 4, 6)
    d = deque(t)

    d.appendleft(2)
    d.append(8)
    d.append(10)
    d.append(12)

    print(list(d))


if __name__ == "__main__":
    main()
