"""

Write a Python program to count the frequency of words in a file.
    Input file: 007.txt
    Note: clear all punctuations except for "-"

{
    'what': 1, 'is': 3, 'python': 4, 'language': 2, 'a': 3, 'widely': 1, 'used': 1, 'high-level': 1,
    'general-purpose': 1, 'interpreted': 1, 'dynamic': 2, 'programming': 3, 'its': 2, 'design': 1,
    'philosophy': 1, 'emphasizes': 1, 'code': 2, 'readability': 1, 'and': 6, 'syntax': 1, 'allows': 1,
    'programmers': 1, 'to': 2, 'express': 1, 'concepts': 1, 'in': 2, 'fewer': 1, 'lines': 1, 'of': 1,
    'than': 1, 'possible': 1, 'languages': 1, 'such': 1, 'as': 1, 'c': 1, 'or': 2, 'java': 1,
    'supports': 1, 'multiple': 1, 'paradigms': 1, 'including': 1, 'object-oriented': 1, 'imperative': 1,
    'functional': 1, 'procedural': 1, 'styles': 1, 'it': 1, 'features': 1, 'type': 1, 'system': 1,
    'automatic': 1, 'memory': 1, 'management': 1, 'has': 1, 'large': 1, 'comprehensive': 1, 'standard': 1,
    'library': 1, 'the': 1, 'best': 1, 'way': 1, 'we': 2, 'learn': 1, 'anything': 1, 'by': 1, 'practice': 1,
    'exercise': 1, 'questions': 1, 'have': 1, 'started': 1, 'this': 1, 'section': 1, 'for': 1, 'those': 1,
    'beginner': 1, 'intermediate': 1, 'who': 1, 'are': 1, 'familiar': 1, 'with': 1
}

"""

from collections import Counter
from itertools import chain
from string import punctuation


__in_file_path = "007.txt"


def main():
    with open(__in_file_path, "r") as f:
        words = map(
            lambda _: _.lower().translate(str.maketrans("", "", punctuation.replace("-", ""))),
            chain(*map(lambda _: _.strip("\n").split(), f.readlines()))
        )

        print(dict(Counter(words)))


if __name__ == "__main__":
    main()
