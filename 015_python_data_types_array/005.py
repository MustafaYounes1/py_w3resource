"""

Write a Python program to get the current memory address and the length in elements of the buffer used to hold an
array's contents. Also, find the size of the memory buffer in bytes.

Note: the array type is unsigned-long-long

[1, 3, 5, 7, 9]

Current memory address and the length in elements of the buffer: (1708519433696, 5)
The size of the memory buffer in bytes: 40

"""

from array import array


def main():
    arr = array('Q', [1, 3, 5, 7, 9])
    print(f"Current memory address and the length in elements of the buffer: {arr.buffer_info()}")
    print(f"The size of the memory buffer in bytes: {arr.itemsize * arr.buffer_info()[1]}")


if __name__ == "__main__":
    main()
