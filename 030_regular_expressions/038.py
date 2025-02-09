"""

Write a Python program to extract values between quotation marks of a string.

'"Python", "PHP", "Java"'   =>  ['Python', 'PHP', 'Java']

"""

import re


def main():
    s = '"Python", "PHP", "Java"'
    print(re.findall(r'"(.+?)"', s))


if __name__ == "__main__":
    main()
