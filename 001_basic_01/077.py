"""

Write a Python program to test whether the system is a big-endian platform or a little-endian platform.

A big-endian system stores the most significant byte of a word at the smallest memory address and the least
significant byte at the largest. A little-endian system, in contrast, stores the least-significant byte at the
smallest address.

The most significant bit/byte (MSB) is the bit/byte in a multiple-bit/byte binary number with the largest value.
This is usually the bit/byte farthest to the left, or the bit/byte transmitted first in a sequence.

E.g.:
=====
Data: 0x12345678

BE:     0x100   0x101   0x102   0x103
        0x12    0x34    0x56    0x78

LE:     0x100   0x101   0x102   0x103
        0x78    0x56    0x34    0x12

Hint: using the 'sys' module

"""

import sys


def main():
    # An indicator of the native byte order. This will have the value 'big' on big-endian (most-significant byte first)
    # platforms, and 'little' on little-endian (least-significant byte first) platforms.
    print(f"Your system is {sys.byteorder}-endian")


if __name__ == "__main__":
    main()
