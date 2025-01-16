"""

Write a Python program to find the first duplicate element in a given array of signed integers.
Return -1 if there are no such elements.

[1, 2, 3, 4, 4, 5]      =>  4
[1, 2, 3, 4]            =>  -1
[1, 1, 2, 3, 3, 2, 2]   =>  1

"""

from array import array


def main():
    data = [
        array('i', [1, 2, 3, 4, 4, 5]),
        array('i', [1, 2, 3, 4]),
        array('i', [1, 1, 2, 3, 3, 2, 2]),
    ]

    for arr in data:
        valid = (_ for _ in arr if arr.count(_) > 1)

        try:
            print(next(valid))

        except StopIteration:
            print(-1)


if __name__ == "__main__":
    main()
