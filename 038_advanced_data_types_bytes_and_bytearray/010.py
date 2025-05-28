"""

Write a Python function that converts a bytearray to a bytes object.

Note: the bytearray contains the following bytes:
    [48, 140, 201, 252, 186, 3, 37, 186, 52]
    ->  b'0\x8c\xc9\xfc\xba\x03%\xba4'

"""


def main():
    bytes_ = [48, 140, 201, 252, 186, 3, 37, 186, 52]
    print(bytes(bytearray(bytes_)))


if __name__ == "__main__":
    main()
