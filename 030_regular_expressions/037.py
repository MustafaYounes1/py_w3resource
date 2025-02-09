"""

Write a python program to convert snake-case string to camel-case string.

python_exercises            =>  PythonExercises
image_classifier_loader     =>  ImageClassifierLoader
image1_loading_api          =>  Image1LoadingApi

"""

import re
from typing import Match


def match_handler(m: Match) -> str:
    return str(m.group(1)).capitalize()


def main():
    data = ["python_exercises", "image_classifier_loader", "image1_loading_api"]
    for _ in data:
        print(re.sub(r"([a-z0-9]+)_?", match_handler, _))


if __name__ == "__main__":
    main()
