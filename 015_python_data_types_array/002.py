"""

Write a Python program to append a new item to the end of the array.

[1, 3, 5, 7, 9] (type: signed-int)

11  =>  [1, 3, 5, 7, 9, 11]

"""

from array import array


def main():
    arr = array('i', [1, 3, 5, 7, 9])
    arr.append(11)
    print(arr.tolist())


if __name__ == "__main__":
    main()
