"""

Write a Python program to get a list with n elements removed from the left and right.

[1, 2, 3]
1 element from left:    [2, 3]
1 element from right:   [1, 2]

[1, 2, 3, 4]
2 elements from left:   [3, 4]
2 elements from right:  [1, 2]

"""


def main():
    data = [
        [[1, 2, 3], 1],
        [[1, 2, 3, 4], 2]
    ]

    for lst, n in data:
        print(lst[n:])
        print(lst[:-n])
        print('*' * 7)


if __name__ == "__main__":
    main()
