"""

Write a Python program to search for a literal string in a string and also find the location within the original
string where the pattern occurs.

Sample text : 'The quick brown fox jumps over the lazy dog.'
Searched words : 'fox'      =>  16 -> 19

"""

import re


def main():
    s = "The quick brown fox jumps over the lazy dog."
    word = "fox"

    ma = re.search(rf"\b{word}\b", s)
    if ma is not None:
        print(" -> ".join(map(str, ma.span())))
    else:
        print(f"{word} is not in the input string")


if __name__ == "__main__":
    main()
