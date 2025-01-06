"""

Write a Python program to split a variable length string into variables.

e.g.: "ab" -> "a", "b"

"""


def main():
    s = "ab"
    v1, v2 = s
    print(v1, v2, sep=" | ")


if __name__ == "__main__":
    main()
