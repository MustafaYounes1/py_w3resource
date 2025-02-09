"""

Write a Python program that matches a string that starts with an "a" followed by zero or one 'b'.

ab      =>  True
abc     =>  True
ac      =>  True
abbc    =>  False
aabbc   =>  True

"""

import re


def main():
    data = ["ab", "abc", "ac", "abbc", "aabbc"]
    pa = re.compile(r"ab?(?=[^b]|\Z)")
    for _ in data:
        print(pa.match(_) is not None)

if __name__ == "__main__":
    main()
