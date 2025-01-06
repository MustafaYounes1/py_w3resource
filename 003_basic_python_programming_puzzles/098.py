"""

Given a string consisting of groups of matched nested parentheses separated by parentheses, write a Python program to
compute the depth of each group.

Input: (()) (()) () ((()()()))                  =>  [2, 2, 1, 3]
Input: () (()) () () () ()                      =>  [1, 2, 1, 1, 1, 1]
Input: (((((((()))))))) () (()) ((()()()))      =>  [8, 1, 2, 3]

"""

import re


__data = [
    "(()) (()) () ((()()()))",
    "() (()) () () () ()",
    "(((((((()))))))) () (()) ((()()()))"
]


def main():
    for w in __data:
        print(
            [len(re.match(r"\(+", _).group(0)) for _ in w.split()]
        )


if __name__ == "__main__":
    main()
