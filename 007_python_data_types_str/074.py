"""

Write a Python program to find the minimum window in a given string that will contain all the characters of
another given string.


str1 = " PRWSOERIUSFK "
str2 = " OSU "
Output: Minimum window is ['SOERIU', 'OERIUS']

"""

import re


def main():
    # s1, s2 = input("Enter the two strings comma-separated: ").split(", ")
    s1, s2 = "PRWSOERIUSFK", "OSU"

    # non-greedy: .*?
    # https://stackoverflow.com/questions/766372/python-non-greedy-regexes
    pattern = f".*?".join([f"[{s2}]" for _ in s2])

    # python only find patterns in a non-overlapping way.
    # For example, we want to find “AA” in “AAAA”, it will give you positions 0 and 2, eg the first two AA and the
    # last two AA.
    # However, the middle two AA is also a match. To get all the overlapping matches, we need “lookahead assertion”.
    # https://junli.netlify.app/en/overlapping-regular-expression-in-python/
    pattern = f"(?=({pattern}))"

    print(re.findall(pattern, s1))


if __name__ == "__main__":
    main()
