"""

Write a Python program to sort a tuple by its float element (the second element that comes as a string) in
descending order.

[('item1', '12.20'), ('item2', '15.10'), ('item3', '24.5')]

[('item3', '24.5'), ('item2', '15.10'), ('item1', '12.20')]

"""


def main():
    lst = [('item1', '12.20'), ('item2', '15.10'), ('item3', '24.5')]
    print(sorted(lst, reverse=True, key=lambda _: float(_[1])))


if __name__ == "__main__":
    main()
