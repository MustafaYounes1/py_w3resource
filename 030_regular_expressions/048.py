"""

Write a Python program to check a decimal with a precision of 2.

123.11      =>  True
123.1       =>  True
123         =>  True
0.21        =>  True
123.1214    =>  False
3.124587    =>  False
e666.86     =>  False

"""

import re


def main():
    data = ["123.11", "123.1", "123", "0.21", "123.1214", "3.124587", "e666.86"]
    pa = re.compile(r"\d+[.]?\d{,2}$")

    for _ in data:
        print(pa.match(_) is not None)


if __name__ == "__main__":
    main()
