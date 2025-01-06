"""

Write a Python program to concatenate (with a dash) N strings in an input list.

"""


def main():
    seq = input("Enter a list of space separated strings: ").split()
    print('-'.join(seq))


if __name__ == "__main__":
    main()
