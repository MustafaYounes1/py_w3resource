"""

Write a Python program to abbreviate 'Road' as 'Rd.' in a given string.

"21 Ramkrishna Road"    =>  21 Ramkrishna Rd.

"""

import re


def main():
    s = "21 Ramkrishna Road"
    print(re.sub(r"\bRoad\b", "Rd.", s))


if __name__ == "__main__":
    main()
