"""

Write a Python program to count the number of substrings in a given string with the same first and last characters.

abc =>  3

"""

from itertools import combinations


def main():
    s = input("Enter a string: ")
    strs = [s[i: j] for i, j in combinations(range(len(s) + 1), 2)]
    print(
        len(
            list(filter(lambda _: _[-1] == s[-1], strs))
        )
    )


if __name__ == "__main__":
    main()
