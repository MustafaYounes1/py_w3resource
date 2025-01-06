"""

Write a Python program to find the indices of two numbers that sum to 0 in a given list of numbers.

Input:
[1, -4, 6, 7, 4]
Output:
[4, 1]

Input:
[1232, -20352, 12547, 12440, 741, 341, 525, 20352, 91, 20]
Output:
[1, 7]

"""

from itertools import combinations


def main():
    seq = list(map(int, input("Enter a list of comma-separated integers: ").split(",")))
    for comb in combinations(seq, 2):
        if sum(comb) == 0:
            print(seq.index(comb[0]), seq.index(comb[1]))


if __name__ == "__main__":
    main()
