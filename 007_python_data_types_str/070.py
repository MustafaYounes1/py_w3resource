"""

Write a Python program that concatenates uncommon characters from two strings.

abcdpqr, xyzabcd     =>  pqrxyz

"""


def main():
    s1, s2 = input("Enter two comma-separated strings: ").split(", ")
    print("".join(set(s1) ^ set(s2)))


if __name__ == "__main__":
    main()
