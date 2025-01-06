"""

Write a Python program to get every nth element in a given list.

[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

n = 1   =>  [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
n = 2   =>  [2, 4, 6, 8, 10]
n = 5   =>  [5, 10]
n = 6   =>  [6]

"""


def main():
    lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    nums = [1, 2, 5, 6]

    for n in nums:
        print([lst[idx] for idx in range(n - 1, len(lst), n)])


if __name__ == "__main__":
    main()
