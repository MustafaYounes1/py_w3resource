"""

Write a Python program to split a given list into specified sized chunks using the itertools module.

[12, 45, 23, 67, 78, 90, 45, 32, 100, 76, 38, 62, 73, 29, 83]

3   =>  [(12, 45, 23), (67, 78, 90), (45, 32, 100), (76, 38, 62), (73, 29, 83)]
4   =>  [(12, 45, 23, 67), (78, 90, 45, 32), (100, 76, 38, 62), (73, 29, 83)]
5   =>  [(12, 45, 23, 67, 78), (90, 45, 32, 100, 76), (38, 62, 73, 29, 83)]

"""

from itertools import islice
from math import ceil


def main():
    lst = [12, 45, 23, 67, 78, 90, 45, 32, 100, 76, 38, 62, 73, 29, 83]
    nums = [3, 4, 5]

    for n in nums:
        print([list(islice(lst, i*n, i*n+n)) for i in range(ceil(len(lst) / n))])


if __name__ == "__main__":
    main()
