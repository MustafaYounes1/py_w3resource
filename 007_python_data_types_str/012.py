"""

Write a Python program to count the occurrences of each word in a given sentence.

"""

from collections import Counter


def main():
    s = input("Enter a sentence: ")
    print(dict(Counter(s.lower().split())))


if __name__ == "__main__":
    main()
