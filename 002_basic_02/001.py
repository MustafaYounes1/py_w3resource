"""

Write a Python function that takes a sequence of numbers and determines whether all the numbers are different
from each other.

"""


def main():
    seq = [int(_) for _ in input("Enter a list of space-separated integers: ").split()]
    print(len(seq) == len(set(seq)))


if __name__ == "__main__":
    main()
