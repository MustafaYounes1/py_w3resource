"""

Write a Python program to find the maximum, minimum aggregation pair in a given list of integers.

[1, 3, 4, 5, 4, 7, 9, 11, 10, 9]

Maximum aggregation pair of the said list of tuple pair:
(11, 10)

Minimum aggregation pair of the said list of tuple pair:
(1, 3)

"""

from itertools import combinations


def main():
    lst = [1, 3, 4, 5, 4, 7, 9, 11, 10, 9]
    combs = list(combinations(lst, 2))
    print(max(combs, key=sum))
    print(min(combs, key=sum))


if __name__ == "__main__":
    main()
