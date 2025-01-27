"""

Write a Python program to create Fibonacci series up to n using Lambda.

2   =>  [0, 1]
5   =>  [0, 1, 1, 2, 3]
6   =>  [0, 1, 1, 2, 3, 5]
9   =>  [0, 1, 1, 2, 3, 5, 8, 13, 21]

"""

from typing import Callable


def main():
    f: Callable[[int], int] = lambda x: 0 if x == 0 else 1 if x == 1 else f(x - 1) + f(x - 2)
    print([f(_) for _ in range(2)])
    print([f(_) for _ in range(5)])
    print([f(_) for _ in range(6)])
    print([f(_) for _ in range(9)])


if __name__ == "__main__":
    main()
