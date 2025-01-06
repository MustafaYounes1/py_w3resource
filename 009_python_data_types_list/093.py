"""

Write a Python program to count the number of sublists that contain a particular element.

[[1, 3], [5, 7], [1, 11], [1, 15, 7]]
Count 1 in the said list: 3
Count 7 in the said list: 2

[['A', 'B'], ['A', 'C'], ['A', 'D', 'E'], ['B', 'C', 'D']]
Count 'A' in the said list: 3
Count 'E' in the said list: 1

"""


def main():
    data = [
        [
            [[1, 3], [5, 7], [1, 11], [1, 15, 7]], 1, 7
        ],
        [
            [['A', 'B'], ['A', 'C'], ['A', 'D', 'E'], ['B', 'C', 'D']], 'A', 'E'
        ]
    ]

    for lst, c1, c2 in data:
        print(c1, sum([_.count(c1) for _ in lst]))
        print(c2, sum([_.count(c2) for _ in lst]))
        print('*' * 25)


if __name__ == "__main__":
    main()
