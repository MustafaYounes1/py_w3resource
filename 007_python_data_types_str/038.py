"""

Write a Python program to count occurrences of a substring in a string.

The quick brown fox jumps over the lazy dog., fox       =>  1

"""


def main():
    s = 'The quick brown fox jumps over the lazy dog.'
    print(s.count('fox'))


if __name__ == "__main__":
    main()
