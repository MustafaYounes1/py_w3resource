"""

Write a Python program to sum all counts in a collection (it should be equal to the len of the list).

"""

from collections import Counter


def main():
    seq = [int(_) for _ in input("Enter a list of space-separated integers: ").split()]
    print(sum(Counter(seq).values()))


if __name__ == "__main__":
    main()
