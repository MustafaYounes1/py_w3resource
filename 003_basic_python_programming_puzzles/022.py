"""

Write a Python program to compute the sum of the ASCII values of the upper-case characters in a given string.

Input:
PytHon ExerciSEs
Output:
373

Input:
JavaScript
Output:
157

"""


def main():
    s = input("Enter a string: ")
    print(sum([ord(_) for _ in s if _.isupper()]))


if __name__ == "__main__":
    main()
