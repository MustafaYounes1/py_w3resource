"""

Write a Python program to find the ratio of positive numbers, negative numbers and zeroes in an array of integers.
    Note: use the array module

[0, 1, 2, -1, -5, 6, 0, -3, -2, 3, 4, 6, 8]     =>  (0.54, 0.31, 0.15)
[2, 1, 2, -1, -5, 6, 4, -3, -2, 3, 4, 6, 8]     =>  (0.69, 0.31, 0.0)

"""

from array import array


def main():
    data = [
        array("i", [0, 1, 2, -1, -5, 6, 0, -3, -2, 3, 4, 6, 8]),
        array("i", [2, 1, 2, -1, -5, 6, 4, -3, -2, 3, 4, 6, 8])
    ]

    for arr in data:
        print(f"({len(list(filter(lambda _: _ > 0, arr))) / len(arr):.2f}, "
              f"{len(list(filter(lambda _: _ < 0, arr))) / len(arr):.2f}, "
              f"{len(list(filter(lambda _: _ == 0, arr))) / len(arr):.2f})")


if __name__ == "__main__":
    main()
