"""

Write a Python program to insert spaces between words starting with capital letters.

Python                              =>  Python
PythonExercises                     =>  Python Exercises
PythonExercisesPracticeSolution     =>  Python Exercises Practice Solution

"""

import re
from typing import Match


def match_handler(m: Match) -> str:
    res = str(m.group())

    if m.end() != len(m.string):
        res += " "

    return res


def main():
    data = ["Python", "PythonExercises", "PythonExercisesPracticeSolution"]
    pa = re.compile(r"[A-Z][^A-Z]+")

    for _ in data:
        print(pa.sub(match_handler, _))


if __name__ == "__main__":
    main()
