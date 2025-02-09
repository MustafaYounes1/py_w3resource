"""

Write a Python program that matches a word at the end of a string, with optional punctuation

"The quick brown fox jumps over the lazy dog."      =>  True
"The quick brown fox jumps over the lazy dog?"      =>  True
"The quick brown fox jumps over the lazy dog. "     =>  False
"The quick brown fox jumps over the lazy dog "      =>  False

"""

import re


def main():
    data = [
        "The quick brown fox jumps over the lazy dog.",
        "The quick brown fox jumps over the lazy dog?",
        "The quick brown fox jumps over the lazy dog. ",
        "The quick brown fox jumps over the lazy dog "
    ]
    pa = re.compile(rf"\w+\S*$")
    for _ in data:
        print(pa.search(_) is not None)

if __name__ == "__main__":
    main()
