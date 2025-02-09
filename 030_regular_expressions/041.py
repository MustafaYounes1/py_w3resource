"""

Write a Python program to remove everything except alphanumeric characters from a string.

"**//Python Exercises// - 12. "     =>  PythonExercises12

"""

import re


def main():
    s = "**//Python Exercises// - 12. "
    print(re.sub(r"[\W_]+", "", s))


if __name__ == "__main__":
    main()
