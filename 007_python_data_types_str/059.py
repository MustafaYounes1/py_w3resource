"""

Write a Python program to find the maximum occurring character in a given string.

Python: Get file creation and modification date/times   =>  t
abcdefghijkb                                            =>  b

"""

from string import punctuation


def main():
    s = input("Enter a string: ")
    s = s.translate(str.maketrans("", "", punctuation + " ")).lower()
    print(max(s, key=lambda _: s.count(_)))


if __name__ == "__main__":
    main()
