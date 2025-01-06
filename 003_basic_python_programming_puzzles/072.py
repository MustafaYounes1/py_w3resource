"""

Write a Python program to find the indices of three numbers that sum to 0 in a given list of numbers.

Input: [12, -7, 3, -89, 14, 4, -78, -1, 2, 7]       =>  [1, 2, 5]
Input: [1, 2, 3, 4, 5, 6, -7]                       =>  [2, 3, 6]

"""

from itertools import combinations


def main():
    seq = list(map(int, input("Enter a list of comma-separated integers: ").split(",")))
    for comb in combinations(seq, 3):
        if sum(comb) == 0:
            print([seq.index(_) for _ in comb])


if __name__ == "__main__":
    main()
