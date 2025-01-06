"""

Write a Python program to find common elements in a nested list.

[[12, 18, 23, 25, 45], [7, 12, 18, 24, 28], [1, 5, 8, 12, 15, 16, 18]]

[18, 12]

"""


def main():
    lst = [[12, 18, 23, 25, 45], [7, 12, 18, 24, 28], [1, 5, 8, 12, 15, 16, 18]]
    print(list(set.intersection(*map(set, lst))))


if __name__ == "__main__":
    main()
