"""

Write a Python program to create a bytearray from a given list of integers.

[72, 123, 21, 108, 222, 67, 44, 38, 10] ->  b'H{\x15l\xdeC,&\n'

"""


def main():
    lst = [72, 123, 21, 108, 222, 67, 44, 38, 10]
    print(bytes(bytearray(lst)))


if __name__ == "__main__":
    main()
