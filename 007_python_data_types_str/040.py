"""

Write a Python program to reverse words in a string.

The quick brown fox jumps over the lazy dog.
dog. lazy the over jumps fox brown quick The
"""


def main():
    s = "The quick brown fox jumps over the lazy dog."
    print(" ".join(s.split()[::-1]))


if __name__ == "__main__":
    main()
