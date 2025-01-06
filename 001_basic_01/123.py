"""

Write a Python program to determine the system largest and smallest integers, longs, and floats.

"""

import sys


def main():
    # A named tuple holding information about the float type.
    print(sys.float_info)

    print("=" * 25)

    # A named tuple that holds information about Python’s internal representation of integers.
    print(sys.int_info)

    print("=" * 25)

    # An integer giving the maximum value a variable of type Py_ssize_t can take. It’s usually 2**31 - 1 on a 32-bit
    # platform and 2**63 - 1 on a 64-bit platform.
    print(sys.maxsize)

if __name__ == "__main__":
    main()
