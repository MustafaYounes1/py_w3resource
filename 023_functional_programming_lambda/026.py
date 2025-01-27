"""

Write a Python program to find a list with maximum and minimum length using lambda.

[[0], [1, 3], [5, 7], [9, 11], [13, 15, 17]]

Max: (3, [13, 15, 17])
Min: (1, [0])

"""


def main():
    lst = [[0], [1, 3], [5, 7], [9, 11], [13, 15, 17]]
    ma = max(lst, key=len)
    mi = min(lst, key=len)
    print(ma)
    print(mi)


if __name__ == "__main__":
    main()
