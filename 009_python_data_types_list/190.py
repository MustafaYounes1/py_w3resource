"""

Write a Python program to find the specified number of largest products from two given lists, multiplying an element
from each list.

[1, 2, 3, 4, 5, 6]
[3, 6, 8, 9, 10, 6]

3   =>  [60, 54, 50]
4   =>  [60, 54, 50, 48]

"""

from itertools import product
from math import prod


def main():
    lst1 = [1, 2, 3, 4, 5, 6]
    lst2 = [3, 6, 8, 9, 10, 6]
    res = sorted(list(map(prod, product(lst1, lst2))), reverse=True)
    print(res[:3])
    print(res[:4])


if __name__ == "__main__":
    main()
