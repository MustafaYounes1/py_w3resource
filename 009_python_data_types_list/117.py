"""

Write a Python program to remove all elements from a given list that are present in another list.

list1: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list2: [2, 4, 6, 8]

[1, 3, 5, 7, 9, 10]

"""


def main():
    list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    list2 = [2, 4, 6, 8]
    print(list(set(list1) - set(list2)))


if __name__ == "__main__":
    main()
