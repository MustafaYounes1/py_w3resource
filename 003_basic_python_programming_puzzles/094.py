"""

Given a string consisting of whitespace and groups of matched parentheses, write a Python program to split it
into groups of perfectly matched parentheses without any whitespace.

Input:
( ()) ((()()())) (()) ()
Output:
['(())', '((()()()))', '(())', '()']

Input:
() (( ( )() ( )) ) ( ())
Output:
['()', '((()()()))', '(())']

"""

__data = [
    "( ()) ((()()())) (()) ()",
    "() (( ( )() ( )) ) ( ())"
]


def main():
    for _ in __data:
        tmp, res = "", []

        for c in _.replace(" ", ""):
            tmp += c
            if tmp.count("(") == tmp.count(")"):
                res.append(tmp)
                tmp = ""

        print(res)


if __name__ == "__main__":
    main()
