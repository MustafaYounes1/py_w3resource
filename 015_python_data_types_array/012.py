"""

Write a Python program to remove the first occurrence of a specified element from a signed-integer array.

[1, 3, 5, 3, 7, 1, 9, 3], 3     =>  [1, 5, 3, 7, 1, 9, 3]

"""

from array import array


def main():
    arr, n = array('i', [1, 3, 5, 3, 7, 1, 9, 3]), 3
    arr.remove(n)
    print(arr.tolist())


if __name__ == "__main__":
    main()
