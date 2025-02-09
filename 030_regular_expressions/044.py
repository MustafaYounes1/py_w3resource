"""

Write a Python program to do case-insensitive string replacement.

Replace "php" in "PHP Exercises php" with *  =>  "* Exercises *"

"""

import re


def main():
    s = "PHP Exercises php"
    print(re.sub(r"php", "*", s, flags=re.IGNORECASE))


if __name__ == "__main__":
    main()
