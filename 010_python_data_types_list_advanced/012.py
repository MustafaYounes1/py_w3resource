"""

Write a Python program to find the first non-repeated element in a list.

[1, 2, 3, 4, 5, 6, 7, 8]        =>  1
[1, 2, 3, 1, 2, 4, 5, 6, 7, 8]  =>  3
[1, 1, 2, 3, 1, 2, 3, 8, 8]     =>  None

"""

from collections import Counter


def main():
    data = [
        [1, 2, 3, 4, 5, 6, 7, 8],
        [1, 2, 3, 1, 2, 4, 5, 6, 7, 8],
        [1, 1, 2, 3, 1, 2, 3, 8, 8]
    ]

    for lst in data:
        c = dict(Counter(lst))
        valid = [_ for idx, _ in enumerate(lst) if c[_] == 1]
        if valid:
            print(valid[0])
        else:
            print(None)


if __name__ == "__main__":
    main()
