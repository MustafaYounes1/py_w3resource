"""

Write a Python program to find the first repeated character in a given string.

abcdabcd    =>  a
abcd        =>  None

"""


def main():
    s = input("Enter a string: ")
    repeated_chars = list(filter(lambda _: s.count(_) > 1, s))
    print(repeated_chars[0] if repeated_chars else None)


if __name__ == "__main__":
    main()
