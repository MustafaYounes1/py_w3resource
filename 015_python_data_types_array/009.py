"""

Write a Python program to append items to a signed-int array.

[1, 2, 6, -8], -11   =>  [1, 2, 6, -8, -11]

"""

from array import array


def main():
    arr, n = array('i', [1, 2, 6, -8]), -11
    arr.append(n)
    print(arr.tolist())


if __name__ == "__main__":
    main()
