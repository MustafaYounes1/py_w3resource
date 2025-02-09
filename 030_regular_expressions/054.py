"""

Write a Python program to convert a given string to snake case.

JavaScript                  =>  java-script
GDScript                    =>  gd-script
PythonExercisesSolutions    =>  python-exercises-solutions

"""

import re
from typing import Match


def match_handler(m: Match) -> str:
    return str(m.group(1)).lower() + "-" + str(m.group(2)).lower()


def main():
    data = ["JavaScript", "GDScript", "PythonExercisesSolutions"]
    pa = re.compile(r"([A-Z]*[^A-Z]*)([A-Z])")

    for _ in data:
        print(pa.sub(match_handler, _))


if __name__ == "__main__":
    main()
