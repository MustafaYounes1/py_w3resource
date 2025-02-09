"""

Write a Python program to replace whitespaces with an underscore.

"Python Exercises   Hello world!"    =>     "Python_Exercises_Hello_world!"

"""

import re


def main():
    s = "Python Exercises   Hello world!"
    print(re.sub(r"\s+", "_", s))


if __name__ == "__main__":
    main()
