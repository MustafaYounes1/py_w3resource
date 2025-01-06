"""

Write a Python program to calculate the maximum and minimum sum of a sublist in a given list of lists.

[[1, 2, 3, 5], [2, 3, 5, 4], [0, 5, 4, 1], [3, 7, 2, 1], [1, 2, 1, 2]]

Maximum sum of sub list of the said list of lists:
[2, 3, 5, 4]

Minimum sum of sub list of the said list of lists:
[1, 2, 1, 2]

"""


def main():
    data = [[1, 2, 3, 5], [2, 3, 5, 4], [0, 5, 4, 1], [3, 7, 2, 1], [1, 2, 1, 2]]
    print(max(data, key=sum))
    print(min(data, key=sum))


if __name__ == "__main__":
    main()
