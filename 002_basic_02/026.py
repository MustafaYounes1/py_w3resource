"""

Write a Python program to compute the summation of the absolute difference of all distinct pairs in a given array
(non-decreasing order).

Sample array: [1, 2, 3]
Then all the distinct pairs will be:
    1 2
    1 3
    2 3

    [1, 2, 3]   =>  4
    [1, 4, 5]   =>  8
"""

from itertools import combinations


def main():
    seq = [int(_) for _ in input("Enter a list of space-separated integers: ").split()]
    s = 0
    for comb in combinations(seq, 2):
        s += abs(comb[0] - comb[1])

    print(s)


if __name__ == "__main__":
    main()
