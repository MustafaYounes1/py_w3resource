"""

Write a Python program to check if a given list of integers can be broken into sets of exactly n consecutive elements.
Note: the difference between each two consecutive items in the sublist should be 1

[1, 2, 3, 4, 5, 6, 7, 8], 4     =>  True
[1, 2, 3, 4, 5, 6, 7, 8], 3     =>  False

"""


def main():
    data = [
        [[1, 2, 3, 4, 5, 6, 7, 8], 4],
        [[1, 2, 3, 4, 5, 6, 7, 8], 3]
    ]

    for lst, size in data:
        sub_lists = [lst[idx: idx + size] for idx in range(0, len(lst), size)]
        print(
            all(
                len(_) == size and all((b - a) == 1 for a, b in zip(_[:-1], _[1:])) for _ in sub_lists
            )
        )


if __name__ == "__main__":
    main()
