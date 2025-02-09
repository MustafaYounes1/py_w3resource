"""

Write a Python program to replace maximum 2 occurrences of space, comma, or dot with a colon.

"Python Exercises, PHP exercises."  =>  Python:Exercises: PHP exercises.

"""

import re

def main():
    s = "Python Exercises, PHP exercises."
    print(re.sub(r"[ ,.]", ":", s, count=2))


if __name__ == "__main__":
    main()
