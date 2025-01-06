"""

Write a Python program to find the two closest distinct numbers in a given list of numbers.

[1.3, 5.24, 0.89, 21.0, 5.27, 1.3]                              =>  [5.24, 5.27]
[12.02, 20.3, 15.0, 19.0, 11.0, 14.99, 17.0, 17.0, 14.4, 16.8]  =>  [14.99, 15.0]

"""

from itertools import combinations


def main():
    seq = list(map(float, input("Enter a list of comma-separated numbers: ").split(",")))
    print(
        min(
            [comb for comb in combinations(seq, 2) if comb[0] != comb[1]],
            key=lambda comb: abs(comb[0] - comb[1])
        )
    )


if __name__ == "__main__":
    main()
