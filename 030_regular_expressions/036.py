"""

Write a Python program to convert a camel-case string to a snake-case string.

PythonExercises         =>  python_exercises
ImageClassifierLoader   =>  image_classifier_loader
Image1LoadingAPI        =>  image1_loading_api

"""

import re
from typing import Match


def match_handler(m: Match) -> str:
    res = str(m.group()).lower()

    if m.end() != len(m.string):
        res += "_"

    return res


def main():
    data = ["PythonExercises", "ImageClassifierLoader", "Image1LoadingAPI"]
    for _ in data:
        print(re.sub(r"[A-Z]+[a-z0-9]*", match_handler, _))


if __name__ == "__main__":
    main()
