"""

Write a Python program to get the memory address and the size of a double array [1.2, 1.5].

(2504488272368, 2)

"""

from array import array


def main():
    arr = array('d', [1.2, 1.5])
    print(arr.buffer_info())


if __name__ == "__main__":
    main()
