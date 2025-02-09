"""

Write a Python program to match the sequences of one upper case letter followed by lower case letters.

AaBbGg      =>  False
Python      =>  True
python      =>  False
PYTHON      =>  False
aA          =>  False
Aa          =>  True

"""

import re


def main():
    data = ["AaBbGg", "Python", "python", "PYTHON", "aA", "Aa"]
    pa = re.compile(r"[A-Z][a-z]+$")
    for _ in data:
        print(pa.match(_) is not None)


if __name__ == "__main__":
    main()
