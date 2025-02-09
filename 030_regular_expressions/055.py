"""

Write a Python program that checks whether a word starts and ends with a vowel in a given string.
Return true if a word matches the condition; otherwise, return false.

"Red Orange White"      -> True
"Red White Black"       -> False
"abcd dkise eosksu"     -> True

"""

import re


def main():
    data = ["Red Orange White", "Red White Black", "abcd dkise eosksu"]
    pa = re.compile(r"\b[aeiou]\w+[aeiou]\b", flags=re.IGNORECASE)

    for _ in data:
        print(pa.search(_) is not None)


if __name__ == "__main__":
    main()
