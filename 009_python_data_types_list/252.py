"""

Write a Python program to get the n maximum elements from a given list of numbers.

[1, 2, 3]
1 maximum elements: [3]
2 maximum elements: [3, 2]

[-2, -3, -1, -2, -4, 0, -5]
3 maximum elements: [0, -1, -2]

[2.2, 2, 3.2, 4.5, 4.6, 5.2, 2.9]
2 maximum elements: [5.2, 4.6]

"""


def main():
    data = [
        [[1, 2, 3], (1, 2)],
        [[-2, -3, -1, -2, -4, 0, -5], (3, )],
        [[2.2, 2, 3.2, 4.5, 4.6, 5.2, 2.9], (2, )]
    ]

    for lst, sizes in data:
        lst = sorted(lst, reverse=True)

        for size in sizes:
            print(lst[:size])

        print('*' * 25)


if __name__ == "__main__":
    main()
