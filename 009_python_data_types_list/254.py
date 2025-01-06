"""

Write a Python program to get the weighted average of two or more numbers.

A weighted average is an average in which some of the items to be averaged are 'more important' or 'less important'
than some of the others. The weights are (non-negative) numbers which measure the relative importance

For example, the weighted average of a list of numbers x1,…,xn with corresponding weights w1,…,wn is:
Weighted average: x1 * w1 + w2 * y2 + x3 * w3 + ... / (w1 + w2 + w3 + ...)

Note: the second list is the weights' list

[10, 50, 40]
[2, 5, 3]

39.0

[82, 90, 76, 83]
[0.2, 0.35, 0.45, 32]

82.97272727272727

"""

from math import prod


def main():
    data = [
        [
            [10, 50, 40],
            [2, 5, 3]
        ],
        [
            [82, 90, 76, 83],
            [0.2, 0.35, 0.45, 32]
        ]
    ]

    for lst1, lst2 in data:
        print(sum(prod(pair) for pair in zip(lst1, lst2)) / sum(lst2))


if __name__ == "__main__":
    main()
