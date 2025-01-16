"""

Write a Python program to get the number of occurrences of a specified element in a signed-integer array.

[1, 3, 5, 3, 7, 9, 3], 3    =>  3

"""

from array import array


def main():
    arr, n = array('i', [1, 3, 5, 3, 7, 9, 3]), 3
    print(arr.count(n))


if __name__ == "__main__":
    main()
