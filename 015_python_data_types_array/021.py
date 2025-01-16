"""

Write a Python program to get the item size in arrays of types unsigned integer and float.

unsigned int item size: 4
float item size: 4

"""

from array import array


def main():
    ui_arr = array('I')
    f_arr = array('f')
    print(f"unsigned int item size: {ui_arr.itemsize}")
    print(f"float item size: {f_arr.itemsize}")


if __name__ == "__main__":
    main()
