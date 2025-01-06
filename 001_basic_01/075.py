"""

Write a Python program to get the Python copyright information.

"""

import sys


def main():
    # using the sys module
    # A string containing the copyright pertaining to the Python interpreter.
    print(sys.copyright)

    print("=" * 25)

    # using the builtin function
    # The function will print the actual Python copyright, which is contained in sys.copyright
    copyright()


if __name__ == "__main__":
    main()
