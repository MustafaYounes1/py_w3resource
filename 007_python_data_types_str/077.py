"""

Write a Python program to count the number of non-empty substrings of a given string.

w3resource  =>  55

"""

from itertools import combinations


def main():
    s = input("Enter the string: ")
    strs = [
        s[i: j] for i, j in combinations(range(len(s) + 1), 2)
    ]

    print(len(sorted(strs)))


if __name__ == "__main__":
    main()
