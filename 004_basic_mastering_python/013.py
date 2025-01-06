"""

Reshape a 1D list to a 2D list with 2 rows.

e.g.    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]  =>  [[0, 1, 2, 3, 4], [5, 6, 7, 8, 9]]

"""


def main():
    lst = list(range(10))
    c = len(lst) // 2
    print(
        [
            lst[:c],
            lst[c:]
        ]
    )


if __name__ == "__main__":
    main()
