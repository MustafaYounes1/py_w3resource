"""

Write a Python program that matches a string that has an "a" followed by three 'b's.

abbb        =>  True
aabbbbbc    =>  True

"""

import re


def main():
    data = ["abbb", "aabbbbbc"]
    pa = re.compile(r"ab{3}")
    for _ in data:
        print(pa.search(_) is not None)

if __name__ == "__main__":
    main()
