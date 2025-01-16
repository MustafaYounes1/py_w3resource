"""

Write a Python program to get the length in bytes of one array item in the internal representation.
Note: the array type is signed-int

[1, 3, 5, 7, 9] => 4

"""

from array import array


def main():
    arr = array('i', [1, 3, 5, 7, 9])
    print(arr.itemsize)


if __name__ == "__main__":
    main()
