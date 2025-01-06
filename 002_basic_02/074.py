"""

Write a Python program to calculate the maximum profit from selling and buying values of stock. An array of numbers
represent the stock prices in chronological order.

For example, given [8, 10, 7, 5, 7, 15], the function will return 10, since the buying value of the stock is 5 dollars
and sell value is 15 dollars.

Sample Input:
[8, 10, 7, 5, 7, 15]    =>  10
[1, 2, 8, 1]            =>  7
[]                      =>  0

"""


def main():
    seq = list(map(int, input("Enter the stock values (space-separated): ").split()))
    p = max(seq) - min(seq) if seq else 0
    print(p)


if __name__ == "__main__":
    main()
