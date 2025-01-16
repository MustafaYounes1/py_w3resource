"""

Write a Python program to return the bytes representation from a bytes array

[119, 51, 114, 101,  115, 111, 117, 114, 99, 101]   =>  b'w3resource'

"""

from array import array


def main():
    # The array should hold bytes hence the char typecode that has a size of 1 byte
    arr = array('b', [119, 51, 114, 101, 115, 111, 117, 114, 99, 101])
    print(arr.tobytes())


if __name__ == "__main__":
    main()
