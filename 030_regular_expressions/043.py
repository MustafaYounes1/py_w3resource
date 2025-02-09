"""

Write a Python program to split a string into uppercase letters.

PythonTutorialAndExercises  =>  ['Python', 'Tutorial', 'And', 'Exercises']

"""

import re


def main():
    s = "PythonTutorialAndExercises"
    print(re.findall(r"[A-Z][^A-Z]*", s))


if __name__ == "__main__":
    main()
