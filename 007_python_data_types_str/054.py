"""

Write a Python program to find the first repeated character in a given string + the index of the first
occurrence is smallest.

abcabc  =>  ('a', 0)
abcb    =>  ('b', 1)
abcc    =>  ('c', 2)
abcxxy  =>  ('x', 3)

"""


def main():
    s = input("Enter the string: ")
    repeated_chars = list(filter(lambda _: s.count(_) > 1, s))
    print((repeated_chars[0], s.index(repeated_chars[0])) if repeated_chars else None)


if __name__ == "__main__":
    main()
