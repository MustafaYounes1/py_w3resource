"""

Write a Python program to remove lowercase substrings from a given string.

KDeoALOklOOHserfLoAJSIskdsf     =>  KDALOOOHLAJSI

"""

import re


def main():
    s = "KDeoALOklOOHserfLoAJSIskdsf"
    print(re.sub(r"[a-z]+", "", s))


if __name__ == "__main__":
    main()
