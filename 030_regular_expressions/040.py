"""

Write a Python program to remove all whitespaces from a string.

" Python    Exercises "     =>  PythonExercises

"""

import re


def main():
    s = " Python    Exercises "
    print(re.sub(r"\s+", "", s))


if __name__ == "__main__":
    main()
