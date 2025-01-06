"""

Write a Python program to identify unique triplets whose three elements sum to zero from an array of n integers.

"""

from itertools import combinations


def main():
    seq = [int(_) for _ in input("Enter a list of space-separated integers: ").split()]
    unique_triplets = []
    for comb in set(combinations(seq, 3)):
        triplet = set(comb)
        if sum(triplet) == 0 and len(triplet) == 3 and triplet not in unique_triplets:
            unique_triplets.append(triplet)
            print(triplet)


if __name__ == "__main__":
    main()
