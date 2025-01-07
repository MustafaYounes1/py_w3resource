"""

Write a Python a function to find the union and intersection of two lists.

[1, 2, 3, 4, 5]
[3, 4, 5, 6, 7, 8]

union:          [1, 2, 3, 4, 5, 6, 7, 8]
intersection:   [3, 4, 5]

["Red", "Green", "Blue"]
["Red", "White", "Pink", "Black"]

union:          ['Pink', 'Blue', 'White', 'Black', 'Red', 'Green']
intersection:   ['Red']

"""


def main():
    data = [
        [
            [1, 2, 3, 4, 5],
            [3, 4, 5, 6, 7, 8]
        ],
        [
            ["Red", "Green", "Blue"],
            ["Red", "White", "Pink", "Black"]
        ]
    ]

    for lst1, lst2 in data:
        print(f"Union:          {list(set(lst1) | set(lst2))}")
        print(f"intersection:   {list(set(lst1) & set(lst2))}")
        print('*' * 25)


if __name__ == "__main__":
    main()
