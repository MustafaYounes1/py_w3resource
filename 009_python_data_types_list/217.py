"""

Write a Python program to split values into two groups, based on the result of the given filtering function.

['red', 'green', 'wow', 'black', 'white']

Filter all values that have 'w' as the first character in the first group and the put the others in the second group

[['wow', 'white'], ['red', 'green', 'black']]

"""


def main():
    lst = ['red', 'green', 'wow', 'black', 'white']
    print(
        [
            [_ for _ in lst if _[0] == 'w'],
            [_ for _ in lst if _[0] != 'w']
        ]
    )


if __name__ == "__main__":
    main()
