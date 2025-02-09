"""

Write a Python program to remove words from a string of length between 1 and 3

"The quick brown fox jumps over the lazy dog."   =>  "quick brown jumps over lazy."

"""

import re
from typing import Match


def match_handler(m: Match) -> str:
    if m.group(1) and m.group(2):
        return " "

    else:
        return ""


def main():
    s = "The quick brown fox jumps over the lazy dog."
    print(re.sub(r"(\s*)\b\w{1,3}\b(\s*)", match_handler, s))


if __name__ == "__main__":
    main()
