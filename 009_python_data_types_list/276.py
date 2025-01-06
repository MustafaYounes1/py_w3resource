"""

Write a Python program to find the largest odd number in a given list of integers.

[0, 9, 2, 4, 5, 6]      -> 9
[-4, 0, 6, 1, 0, 2]     -> 1
[1, 2, 3]               -> 3
[-4, 0, 5, 1, 0, 1]     -> 5

"""


def main():
    data = [
        [0, 9, 2, 4, 5, 6],
        [-4, 0, 6, 1, 0, 2],
        [1, 2, 3],
        [-4, 0, 5, 1, 0, 1]
    ]

    for lst in data:
        print(max(list(filter(lambda _: _ % 2 != 0, lst))))


if __name__ == "__main__":
    main()
