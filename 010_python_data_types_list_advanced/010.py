"""

Write a Python a function to find the sub-sequence of the minimum sum in a list.

[1, 2, 6, 12]                           =>  [1]
[1, -2, 4, 3, 5, 4, 6, 9, 2, -10]       =>  [-10]
[2, 4, -3, -5, -4, 6, 9, 2]             =>  [-3, -5, -4]
[1, 2, 4, 3, 5, -24, 4, 9, -22]         =>  [-24, 4, 9, -22]

"""


def main():
    data = [
        [1, 2, 6, 12],
        [1, -2, 4, 3, 5, 4, 6, 9, 2, -10],
        [2, 4, -3, -5, -4, 6, 9, 2],
        [1, 2, 4, 3, 5, -24, 4, 9, -22]
    ]

    for lst in data:
        print(
            min(
                [lst[i:j] for i in range(len(lst)) for j in range(i + 1, len(lst) + 1)],
                key=sum
            )
        )


if __name__ == "__main__":
    main()
