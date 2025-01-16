"""

Write a Python program to convert an array to an ordinary list with the same items.

[1, 3, 5, 3, 7, 1, 9, 3]    =>  [1, 3, 5, 3, 7, 1, 9, 3]

"""

from array import array


def main():
    arr = array('i', [1, 3, 5, 3, 7, 1, 9, 3])
    print(arr.tolist())


if __name__ == "__main__":
    main()
