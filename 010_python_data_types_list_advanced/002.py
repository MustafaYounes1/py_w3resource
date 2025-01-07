"""

Write a Python function to find the length of the longest increasing sub-sequence in a list.

[10, 20, 30, 40, 50, 60, 70, 80]    =>  8
[10, 20, 30, 40, 50, 30, 30, 20]    =>  5
[-1, -2, -3, -4, -5, -11, -12, -13] =>  1

"""


def main():
    data = [
        [10, 20, 30, 40, 50, 60, 70, 80],
        [10, 20, 30, 40, 50, 30, 30, 20],
        [-1, -2, -3, -4, -5, -11, -12, -13],
    ]

    for lst in data:
        valid = list(
            filter(
                lambda _: all(pair[1] > pair[0] for pair in zip(_[:-1], _[1:])),
                [lst[i:j] for i, _ in enumerate(lst) for j in range(i + 1, len(lst) + 1)]
            )
        )

        print(len(max(valid, key=len)))


if __name__ == "__main__":
    main()
