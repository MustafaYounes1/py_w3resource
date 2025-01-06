"""

Write a Python program to check if the elements of the first list are contained in the second one regardless of order.
Note: consider duplicated elements! i.e. if an element exists twice in the first list, it should also exist twice in
the second list

[1, 2], [2, 4, 1]           =>  True
[1], [2, 4, 1]              =>  True
[1, 1], [4, 2, 1]           =>  False
[1, 1], [3, 2, 4, 1, 5, 1]  =>  True

"""


def main():
    data = [
        [[1, 2], [2, 4, 1]],
        [[1], [2, 4, 1]],
        [[1, 1], [4, 2, 1]],
        [[1, 1], [3, 2, 4, 1, 5, 1]]
    ]

    for lst1, lst2 in data:
        print(all(lst1.count(_) == lst2.count(_) for _ in set(lst1)))


if __name__ == "__main__":
    main()
