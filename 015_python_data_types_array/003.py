"""

Write a Python program to reverse the order of the signed-int items in the array.

[1, 3, 5, 3, 7, 1, 9, 3]    =>   [3, 9, 1, 7, 3, 5, 3, 1]

"""

from array import array


def main():
    arr = array('i', [1, 3, 5, 3, 7, 1, 9, 3])
    arr.reverse()
    print(arr.tolist())


if __name__ == "__main__":
    main()
