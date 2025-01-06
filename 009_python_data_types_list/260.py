"""

Write a Python program to check if all the elements of a list are included in another given list.
Note: all elements from the second list should be present in the first list

[10, 20, 30, 40, 50, 60], [20, 40]  =>  True
[10, 20, 30, 40, 50, 60], [20, 80]  =>  False

"""


def main():
    data = [
        [[10, 20, 30, 40, 50, 60], [20, 40]],
        [[10, 20, 30, 40, 50, 60], [20, 80]]
    ]

    for lst1, lst2 in data:
        print(all(map(lambda _: _ in lst1, lst2)))


if __name__ == "__main__":
    main()
