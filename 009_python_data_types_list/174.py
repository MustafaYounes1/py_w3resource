"""

Write a Python program to add a number to each element in a given list of numbers.

[3, 8, 9, 4, 5, 0, 5, 0, 3]
3       =>  [6, 11, 12, 7, 8, 3, 8, 3, 6]

[3.2, 8, 9.9, 4.2, 5, 0.1, 5, 3.11, 0]
0.51    =>  [3.71, 8.51, 10.41, 4.71, 5.51, 0.61, 5.51, 3.62, 0.51]

"""


def main():
    data = [
        ([3, 8, 9, 4, 5, 0, 5, 0, 3], 3),
        ([3.2, 8, 9.9, 4.2, 5, 0.1, 5, 3.11, 0], 0.51)
    ]

    for lst, n in data:
        print(list(map(lambda _: _ + n, lst)))


if __name__ == "__main__":
    main()
