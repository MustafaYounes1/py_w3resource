"""

Write a Python program that finds the value of n when n degrees of number 2 are written sequentially on a line
without spaces between them.

    "2481632" == 2 4 8 16 32 => 5


"""

import math


def n_degree(n):
    string = str(n)
    i1, i2 = 0, 1
    d = 0

    while i2 <= len(string):
        tmp = math.log2(int(string[i1: i2]))
        if tmp.is_integer() and tmp != 0:
            d += 1
            i1 = i2
            i2 += 1
        else:
            i2 += 1

    return d


def main():
    n = int(input("Enter a number: "))
    print(n_degree(n))


if __name__ == "__main__":
    main()
