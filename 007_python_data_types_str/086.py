"""

Write a Python program to delete all occurrences of a specified character in a given string.

Delete all occurrences of a specified character in a given string, a

Delete ll occurrences of specified chrcter in given string

"""


def main():
    s, c = input("Enter the string and the character comma-separated: ").split(", ")
    print(" ".join(
        list(filter(lambda x: x, [_.replace(c, "") for _ in s.split()]))
    )
    )


if __name__ == "__main__":
    main()
