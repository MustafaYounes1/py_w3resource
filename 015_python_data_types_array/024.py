"""

Write a Python program to find the missing number in a given array of unsigned integers between 10 and 20.

[10, 11, 12, 13, 14, 16, 17, 18, 19, 20]   =>   15
[10, 11, 12, 13, 14, 15, 16, 17, 18, 19]   =>   20

"""

from array import array


def main():
    data = [
        array('I', [10, 11, 12, 13, 14, 16, 17, 18, 19, 20]),
        array('I', [10, 11, 12, 13, 14, 15, 16, 17, 18, 19])
    ]

    for arr in data:
        print(set(range(10, 21)) - set(arr))


if __name__ == "__main__":
    main()
