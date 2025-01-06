"""

Given a string consisting of whitespace and groups of matched parentheses, write a Python program to split it into
groups of perfectly matched parentheses without any whitespace.

( ()) ((()()())) (()) ()    =>  ['(())', '((()()()))', '(())', '()']
() (( ( )() ( )) ) ( ())    =>  ['()', '((()()()))', '(())']

"""

import re


def main():
    s = input("Enter a string: ").replace(" ", "")
    res = []
    tmp = ""

    for _ in s:
        tmp += _
        if tmp.count("(") == tmp.count(")"):
            res.append(tmp)
            tmp = ""

    print(res)


if __name__ == "__main__":
    main()
