"""

Write a Python program to find the numbers in a given string and store them in a list.
Afterward, display the numbers that are larger than the length of the found list of numbers.
Use the lambda function to solve the problem.

'sdf 23 safs8 5 sdfsd8 sdfs 56 21sfs 20 5'  =>  [20, 21, 23, 56]

"""

import re


def main():
    s = 'sdf 23 safs8 5 sdfsd8 sdfs 56 21sfs 20 5'
    nums = list(map(int, re.findall(r"[0-9]+", s)))
    print(sorted(filter(lambda _: _ > len(nums), nums)))


if __name__ == "__main__":
    main()
