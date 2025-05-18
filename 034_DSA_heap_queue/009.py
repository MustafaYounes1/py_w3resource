"""

Write a Python program that sorts multiple input lists and merge them into a single sorted iterator using the heap
queue algorithm.

num1 = [25, 24, 15, 4, 5, 29, 110]
num2 = [19, 20, 11, 56, 25, 233, 154]
num3 = [24, 26, 54, 48]

Ascending order:    [4, 5, 11, 15, 19, 20, 24, 24, 25, 25, 26, 29, 48, 54, 56, 110, 154, 233]
Descending order:   [233, 154, 110, 56, 54, 48, 29, 26, 25, 25, 24, 24, 20, 19, 15, 11, 5, 4]

"""

from heapq import merge


def main():
    data = [
        [25, 24, 15, 4, 5, 29, 110],
        [19, 20, 11, 56, 25, 233, 154],
        [24, 26, 54, 48],
    ]

    print(list(merge(*map(sorted, data))))
    print(list(merge(*map(lambda _: sorted(_, reverse=True), data), reverse=True)))


if __name__ == "__main__":
    main()
