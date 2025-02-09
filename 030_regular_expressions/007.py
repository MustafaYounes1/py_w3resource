"""

Write a Python program to match sequences of lowercase letters joined by one underscore.

aab_cbbbc   =>  True
aab_Abbbc   =>  False
Aaab_abbbc  =>  False

"""

import re


def main():
    data = ["aab_cbbbc", "aab_Abbbc", "Aaab_abbbc"]
    pa = re.compile(r"[a-z]+_[a-z]+$")
    for _ in data:
        print(pa.match(_) is not None)


if __name__ == "__main__":
    main()
