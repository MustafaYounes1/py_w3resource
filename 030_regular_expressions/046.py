"""

Write a Python program to find all adverbs and their positions in a given sentence.

Sample text : "Clearly, he has no excuse for such behavior."

0-7: Clearly

"""

import re


def main():
    s = "Clearly, he has no excuse for such behavior."

    for _ in re.finditer(r"\b[a-zA-z]+ly\b", s):
        print("-".join(map(str, _.span())), f": {_.group()}")


if __name__ == "__main__":
    main()
