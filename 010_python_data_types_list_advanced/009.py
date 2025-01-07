"""

Write a Python a function to find the maximum sum sub-sequence in a list.

[1, 2, 3]                           =>  6
[1, 2, 4, 3, 5, 4, 6, 9, 2, -10]    =>  36
[1, 2, -4, 3, 5, 4, 6, 9, 2, -10]   =>  29
[1, 2, 4, 3, 5, -24, 6, 9, -2]      =>  15

"""


def main():
    data = [
        [1, 2, 3],
        [1, 2, 4, 3, 5, 4, 6, 9, 2, -10],
        [1, 2, -4, 3, 5, 4, 6, 9, 2, -10],
        [1, 2, 4, 3, 5, -24, 6, 9, -2]
    ]

    for lst in data:
        print(
            max(
                map(
                    sum,
                    [lst[i:j] for i in range(len(lst)) for j in range(i + 1, len(lst) + 1)]
                )
            )
        )


if __name__ == "__main__":
    main()
