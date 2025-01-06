"""

Write a Python program to add leading zeroes to a string.

e.g. 1 -> 001

"""


def main():
    i = 1
    print(str(i).zfill(3))
    print(str(i).rjust(3, '0'))
    print("{:>03}".format(i))
    print(f"{i:>03}")


if __name__ == "__main__":
    main()
