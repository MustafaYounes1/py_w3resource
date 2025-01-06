"""

Write a Python program to convert a given string into a list of words.

The quick brown fox jumps over the lazy dog.

Sample Output:
['The', 'quick', 'brown', 'fox', 'jumps', 'over', 'the', 'lazy', 'dog.']

"""


def main():
    s = "The quick brown fox jumps over the lazy dog."
    print(s.split())


if __name__ == "__main__":
    main()
