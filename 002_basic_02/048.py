"""

Write a Python program that reads n digits (given) chosen from 0 to 9 and prints the number of combinations where
the sum of the digits equals another given number (s). Do not use the same digits in a combination.

Input:
Two integers as number of combinations and their sum by a single space in a line. Input 0 0 to exit.
Input number of combinations and sum, input 0 0 to exit:
5 6
2 4
0 0
2

"""

from itertools import combinations


def main():
    res = 0

    print("Enter the number of digits and the sum (or 0 0 to exit):")

    while True:
        x, y = [int(_) for _ in input("").split()]
        if x == 0 and y == 0:
            break

        for _ in combinations(range(10), x):
            if sum(_) == y:
                res += 1

    print(res)

if __name__ == "__main__":
    main()
