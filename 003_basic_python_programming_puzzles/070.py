"""

Write a Python program to find the first negative balance from a given list of numbers that represent bank deposits
and withdrawals.

Note:   Each following list has two records of deposits and withdrawals

[[12, -7, 3, -89, 14, 88, -78], [-1, 2, 7]]     =>  [-81, -1]
[[1200, 100, -900], [100, 100, -2400]]          =>  [None, -2200]

"""

from itertools import accumulate
from operator import add


__data = [
    [[12, -7, 3, -89, 14, 88, -78], [-1, 2, 7]],
    [[1200, 100, -900], [100, 100, -2400]]
]


def main():
    for sample in __data:
        res = []
        for record in sample:
            acc = list(accumulate(record, add))
            negatives = [idx for idx, _ in enumerate(acc) if _ < 0]

            if negatives:
                res.append(acc[negatives[0]])
            else:
                res.append(None)

        print(res)


if __name__ == "__main__":
    main()
