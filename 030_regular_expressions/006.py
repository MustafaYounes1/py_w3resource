"""

Write a Python program that matches a string that has an "a" followed by two to three 'b'.

ab          =>  False
aabbbbbc    =>  True

"""

import re


def main():
    data = ["ab", "aabbbbbc"]
    pa = re.compile(r"ab{2,3}")
    for _ in data:
        print(pa.search(_) is not None)


if __name__ == "__main__":
    main()
