"""

Write a Python program that fills a list with the specified value.

0, 7    =>  [0, 0, 0, 0, 0, 0, 0]
3, 8    =>  [3, 3, 3, 3, 3, 3, 3, 3]
-2, 5   =>  [-2, -2, -2, -2, -2]
3.2, 5  =>  [3.2, 3.2, 3.2, 3.2, 3.2]

"""


def main():
    data = [
        (0, 7),
        (3, 8),
        (-2, 5),
        (3.2, 5),
    ]

    for el, c in data:
        print([el] * c)


if __name__ == "__main__":
    main()
