"""

Write a Python program that accepts a hyphen-separated sequence of words as input and prints the words in a
hyphen-separated sequence after sorting them alphabetically.

green-red-yellow-black-white    =>  black-green-red-white-yellow

"""


def sort(s: str) -> str:
    return "-".join(sorted(s.split("-")))


def main():
    print(sort("green-red-yellow-black-white"))


if __name__ == "__main__":
    main()
