"""

Write a Python program to remove all elements from a given list present in another list using lambda.

[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
[2, 4, 6, 8]
Remove all elements from the first list present in the second list
[1, 3, 5, 7, 9, 10]

"""


def main():
    lst1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    lst2 = [2, 4, 6, 8]
    print(list(filter(lambda _: _ not in lst2, lst1)))


if __name__ == "__main__":
    main()
