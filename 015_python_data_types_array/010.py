"""

Write a Python program to insert a newly created item before the second element in an existing signed-int array.

[1, 3, 5, 7, 9], 4  =>  [1, 4, 3, 5, 7, 9]

"""

from array import array


def main():
    arr, n = array('i', [1, 3, 5, 7, 9]), 4
    arr.insert(1, n)
    print(arr.tolist())


if __name__ == "__main__":
    main()
