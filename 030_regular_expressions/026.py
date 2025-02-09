"""

Write a Python program to match if two words from a list of words start with the letter 'P'.

["Python PHP", "Java JavaScript", "c c++"]  =>  ('Python', 'PHP')

"""

import re


def main():
    lst = ["Python PHP", "Java JavaScript", "c c++"]
    pa = re.compile(r"(\bP.*)\s(\bP.*)$")
    for _ in lst:
        ma = pa.match(_)
        if ma:
            print(ma.groups())


if __name__ == "__main__":
    main()
