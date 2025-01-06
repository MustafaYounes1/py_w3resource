"""

Check if two strings are anagrams.

An anagram of a string is another string that contains the same characters, only the order of characters can be
different.

s1 = "listen"
s2 = "silent"

True

"""


def main():
    s1 = "listen"
    s2 = "silent"
    print(set(s1) == set(s2))


if __name__ == "__main__":
    main()
