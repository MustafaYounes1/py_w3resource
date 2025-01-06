"""

Write a Python program to find common items in two lists.

["Red", "Green", "Orange", "White"], ["Black", "Green", "White", "Pink"]    =>  {'Green', 'White'}

"""


def main():
    lst1, lst2 = ["Red", "Green", "Orange", "White"], ["Black", "Green", "White", "Pink"]
    print(set(lst1) & set(lst2))


if __name__ == "__main__":
    main()
