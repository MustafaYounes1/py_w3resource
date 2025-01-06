"""

Write a Python program to count characters at the same position in a given string (lower and uppercase characters) as
in the English alphabet.

xbcefg  =>  2

"""

from string import ascii_lowercase


def main():
    s = input("Enter a string: ").lower()
    print(
        len([_ for idx, _ in enumerate(s) if idx == ascii_lowercase.index(_)])
    )

    # or
    c = 0
    for idx in range(len(s)):
        if (idx == ord(s[idx]) - ord("a")) or (idx == ord(s[idx]) - ord("A")):
            c += 1

    print(c)


if __name__ == "__main__":
    main()
