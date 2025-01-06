"""

Write a Python program to add all elements of a list of integers except the number at index.

Example: ([1, 2, 3]) -> [1+2+3-1, 1+2+3-2, 1+2+3-3]     -> [5, 4, 3].

[0, 9, 2, 4, 5, 6]      -> [26, 17, 24, 22, 21, 20]
[-4, 0, 6, 1, 0, 2]     -> [9, 5, -1, 4, 5, 3]
[1, 2, 3]               -> [5, 4, 3]
[-4, 0, 5, 1, 0, 1]     -> [7, 3, -2, 2, 3, 2]

"""


def main():
    data = [
        [0, 9, 2, 4, 5, 6],
        [-4, 0, 6, 1, 0, 2],
        [1, 2, 3],
        [-4, 0, 5, 1, 0, 1]
    ]

    for lst in data:
        s = sum(lst)
        print(list(map(lambda _: s - _, lst)))


if __name__ == "__main__":
    main()
