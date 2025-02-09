"""

Write a Python program that matches a string that starts with an "a" followed by one or more "b"s.

ab      =>  True
abc     =>  True

"""

import re


def main():
    data = ["ab", "abc"]
    pa = re.compile(r"ab+")
    for _ in data:
        print(pa.match(_) is not None)


if __name__ == "__main__":
    main()
