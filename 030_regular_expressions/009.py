"""

Write a Python program that matches a string that starts with an 'a' followed by anything ending in 'b'

aabbbbd     =>  False
aabAbbbc    =>  False
accddbbjjjb =>  True

"""

import re


def main():
    data = ["aabbbbd", "aabAbbbc", "accddbbjjjb"]
    pa = re.compile(r"a.*b\Z")
    for _ in data:
        print(pa.match(_) is not None)


if __name__ == "__main__":
    main()
