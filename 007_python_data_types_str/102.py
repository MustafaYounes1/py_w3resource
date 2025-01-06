"""

Write a Python program to remove punctuation from a given string.

String! With. Punctuation?  =>  String With Punctuation

"""

from string import punctuation


def main():
    s = input("Enter a string: ")
    print(" ".join(["".join([__ for __ in _ if __ not in punctuation]) for _ in s.split()]))


if __name__ == "__main__":
    main()
