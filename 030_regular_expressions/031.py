"""

Write a Python program to replace all occurrences of a space, comma, or dot with a colon.

"Python Exercises, PHP exercises."  =>  Python:Exercises::PHP:exercises:

"""

import re


def main():
    s = "Python Exercises, PHP exercises."
    print(re.sub(r"[ ,.]", ":", s))


if __name__ == "__main__":
    main()
