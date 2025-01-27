"""

Write a Python program to compute the sum of elements of an array of integers.
    Hint: use the array module

[1, 2, 3, 4, 5, -15]  =>    0

"""

import array


def main():
    arr = array.array('i', [1, 2, 3, 4, 5, -15])
    print(sum(arr))


if __name__ == "__main__":
    main()
