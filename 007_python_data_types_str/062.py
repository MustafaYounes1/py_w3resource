"""

Write a Python program to compute the sum of the digits in a given string.

123abcd45   =>  15

"""


def main():
    s = "123abcd45"
    print(sum([int(_) for _ in s if _.isdigit()]))


if __name__ == "__main__":
    main()
