"""

Write a Python program to get the n minimum elements from a given list of numbers.

[1, 2, 3]
1 maximum elements: [1]
2 maximum elements: [1, 2]

[-2, -3, -1, -2, -4, 0, -5]
3 maximum elements: [-5, -4, -3]

[2.2, 2, 3.2, 4.5, 4.6, 5.2, 2.9]
2 maximum elements: [2, 2.2]
"""


def main():
    data = [
        [[1, 2, 3], (1, 2)],
        [[-2, -3, -1, -2, -4, 0, -5], (3, )],
        [[2.2, 2, 3.2, 4.5, 4.6, 5.2, 2.9], (2, )]
    ]

    for lst, sizes in data:
        lst = sorted(lst)

        for size in sizes:
            print(lst[:size])

        print('*' * 25)


if __name__ == "__main__":
    main()
