"""

Write a Python program to remove a specified item using the index of a signed-integer array.

[1, 3, 5, 7, 9]

Remove the third item   =>  [1, 3, 7, 9]

"""

from array import array


def main():
    arr = array('i', [1, 3, 5, 7, 9])
    arr.pop(2)
    print(arr.tolist())


if __name__ == "__main__":
    main()
