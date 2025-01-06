"""

The price of a given stock on each day is stored in an array.
Write a Python program to find the maximum profit in one transaction i.e., buy one and sell one share of the stock
from the given price value of the said array. You cannot sell a stock before you buy one.

Input (Stock price of each day): [224, 236, 247, 258, 259, 225]     =>  Output: 35
Explanation:
236 - 224 = 12
247 - 224 = 23
258 - 224 = 34
259 - 224 = 35
225 - 224 = 1
247 - 236 = 11
258 - 236 = 22
259 - 236 = 23
225 - 236 = -11
258 - 247 = 11
259 - 247 = 12
225 - 247 = -22
259 - 258 = 1
225 - 258 = -33
225 - 259 = -34

"""

from sys import maxsize


def main():
    seq = list(map(int, input("Enter the transaction: ").split()))

    max_profit = -maxsize
    for idx, price in enumerate(seq[1:], 1):
        for p in seq[:idx]:
            if (price - p) > max_profit:
                max_profit = price - p

    print(max_profit)


if __name__ == "__main__":
    main()
