"""

Write a Python program to find the indices of the closest pair from a list of numbers.

Input: [1, 7, 9, 2, 10]                             =>  [0, 3]
Input: [1.1, 4.25, 0.79, 1.0, 4.23]                 =>  [4, 1]
Input: [0.21, 11.3, 2.01, 8.0, 10.0, 3.0, 15.2]     =>  [2, 5]

"""

from itertools import combinations


def main():
    seq = list(map(float, input("Enter a list of comma-separated numbers: ").split(",")))
    diffs = []

    for comb in combinations(seq, 2):
        diffs.append((comb, abs(comb[0] - comb[1])))

    min_diff = min(diffs, key=lambda pair: pair[1])
    print(
        [seq.index(min_diff[0][0]), seq.index(min_diff[0][1])]
    )


if __name__ == "__main__":
    main()
