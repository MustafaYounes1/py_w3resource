"""

Write a Python program to append a signed-integer array to itself.

[1, 3, 5, 7, 9] =>  [1, 3, 5, 7, 9, 1, 3, 5, 7, 9]

"""

from array import array


def main():
    arr = array('i', [1, 3, 5, 7, 9])
    arr.extend(arr)
    print(arr.tolist())


if __name__ == "__main__":
    main()
