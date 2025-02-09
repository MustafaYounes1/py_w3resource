"""

Write a Python program to remove multiple spaces from a string.

"Python      Exercises"     =>  Python Exercises

"""

import re


def main():
    s = "Python      Exercises"
    print(re.sub(r"\s+", " ", s))


if __name__ == "__main__":
    main()
