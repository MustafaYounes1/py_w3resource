"""

Write a Python program to reverse a given list of lists.

[['orange', 'red'], ['green', 'blue'], ['white', 'black', 'pink']]
[['white', 'black', 'pink'], ['green', 'blue'], ['orange', 'red']]

[[1, 2, 3, 4], [0, 2, 4, 5], [2, 3, 4, 2, 4]]
[[2, 3, 4, 2, 4], [0, 2, 4, 5], [1, 2, 3, 4]]

"""


def main():
    data = [
        [['orange', 'red'], ['green', 'blue'], ['white', 'black', 'pink']],
        [[1, 2, 3, 4], [0, 2, 4, 5], [2, 3, 4, 2, 4]]
    ]

    for _ in data:
        print(_[::-1])


if __name__ == "__main__":
    main()
