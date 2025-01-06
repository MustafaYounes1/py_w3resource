"""

Write a Python program to determine if a Python shell is executing in 32bit or 64bit mode on OS.

"""

import platform
import struct


def main():
    # using platform
    print(f"Python shell is executing in {platform.architecture()[0]} mode")

    # using struct
    # This module converts between Python values and C structs represented as Python bytes objects.
    # it provides pack and unpack functions for working with variable-length binary data.
    # Use the 'calcsize' function to determine the size (in bytes) of the C int type for the current platform.
    # The format string "P" is used to represent the C void pointer type, and multiplying it by 8 gives the size
    # in bits. The result will be 32 for 32-bit platforms and 64 for 64-bit platforms
    print(f"Python shell is executing in {struct.calcsize('P') * 8}bit mode")


if __name__ == "__main__":
    main()
