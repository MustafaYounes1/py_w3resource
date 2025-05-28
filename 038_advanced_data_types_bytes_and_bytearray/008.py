"""

Write a Python program to compress and decompress a bytes sequence using zlib.

Original Bytes:     b'Python Exercises.'
Compressed Bytes:   b'x\x9c\x0b\xa8,\xc9\xc8\xcfSp\xadH-J\xce,N-\xd6\x03\x00;6\x06|'
Decompressed Bytes: b'Python Exercises.'

"""

import zlib


def main():
    b = b"Python Exercises."

    cmp_b = zlib.compress(b)
    print(cmp_b)

    dcmp_b = zlib.decompress(cmp_b)
    print(dcmp_b)


if __name__ == "__main__":
    main()
