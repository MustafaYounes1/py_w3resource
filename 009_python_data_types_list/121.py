"""

Write a Python program to find nested list elements that are present in another list.

[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
[[12, 18, 23, 25, 45], [7, 11, 19, 24, 28], [1, 5, 8, 18, 15, 16]]

[[12], [7, 11], [1, 5, 8]]

"""


def main():
    lst1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
    lst2 = [[12, 18, 23, 25, 45], [7, 11, 19, 24, 28], [1, 5, 8, 18, 15, 16]]

    print([list(set(_) & set(lst1)) for _ in lst2])


if __name__ == "__main__":
    main()
