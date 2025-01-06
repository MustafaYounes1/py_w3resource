"""

Write a Python program to count the number 4 in a given list.

"""


def main():
    seq = [int(_) for _ in input("Enter a list of space-separated integers: ").split()]
    print(seq.count(4))


if __name__ == "__main__":
    main()
