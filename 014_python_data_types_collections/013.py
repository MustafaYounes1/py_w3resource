"""

Write a Python program to rotate a Deque Object a specified number of times to the right.

[2, 4, 6, 8, 10]

Note: perform the following rotations continuously
1 rotation     =>  [10, 2, 4, 6, 8]
2 rotations    =>  [6, 8, 10, 2, 4]

"""

from collections import deque


def main():
    d = deque([2, 4, 6, 8, 10])

    for r in (1, 2):
        d.rotate(r)
        print(list(d))


if __name__ == "__main__":
    main()
