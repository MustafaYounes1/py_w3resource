"""

Write a Python program to remove characters that have odd index values in a given string.

abcdef  =>  ace

"""


def main():
    s = input("Enter a string: ")
    print("".join([_ for idx, _ in enumerate(s) if idx % 2 == 0]))


if __name__ == "__main__":
    main()
