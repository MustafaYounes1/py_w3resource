"""

Write a Python program to split values into two groups, based on the result of the given filter list.

['red', 'green', 'blue', 'pink'], [True, True, False, True]

[['red', 'green', 'pink'], ['blue']]

"""


def main():
    lst, filter_lst = ['red', 'green', 'blue', 'pink'], [True, True, False, True]
    print(
        [
            [_ for _, __ in zip(lst, filter_lst) if __],
            [_ for _, __ in zip(lst, filter_lst) if not __],
        ]
    )


if __name__ == "__main__":
    main()
