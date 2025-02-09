"""

Write a Python program that tests whether a string starts with '5'

5-2345861   =>  True
6-2345861   =>  False

"""

import re


def main():
    data = ["5-2345861", "6-2345861"]
    pa = re.compile(r"5")
    for _ in data:
        print(pa.match(_) is not None)


if __name__ == "__main__":
    main()
