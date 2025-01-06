"""

Write a Python program to find a valid substring of a given string that contains matching brackets,
at least one of which is nested.

]][][[]]]                                                                       =>  [[]]
]]]]]]]]]]]]]]]]][][][][]]]]]]]]]]][[[][[][[[[[][][][]][[[[[[[[[[[[[[[[[[       =>  [[][][][]]

"""

__data = [
    "]][][[]]]",
    "]]]]]]]]]]]]]]]]][][][][]]]]]]]]]]][[[][[][[[[[][][][]][[[[[[[[[[[[[[[[[["
]

import re


def main():
    for sample in __data:
        print(re.search(r"\[(\[\])+\]", sample).group(0))


if __name__ == "__main__":
    main()
