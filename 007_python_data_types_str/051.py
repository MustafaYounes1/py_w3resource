"""

Write a Python program to find the first non-repeating character in a given string.

abcdef      =>  a
abcabcdef   =>  d
aabbcc      =>  None
"""


def main():
    s = input("Enter a string: ")
    unique_chars = list(filter(lambda _: s.count(_) == 1, s))
    print(unique_chars[0] if unique_chars else None)


if __name__ == "__main__":
    main()
