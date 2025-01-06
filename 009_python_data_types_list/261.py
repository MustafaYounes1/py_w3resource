"""

Write a Python program to get the most frequent element in a given list of numbers.

[2, 3, 8, 4, 7, 9, 8, 2, 6, 5, 1, 6, 1, 2, 3, 2, 4, 6, 9, 1, 2]     =>  2
[1, 2, 3, 1, 2, 3, 2, 1, 4, 3, 3]                                   =>  3

"""

from collections import Counter


def main():
    data = [
        [2, 3, 8, 4, 7, 9, 8, 2, 6, 5, 1, 6, 1, 2, 3, 2, 4, 6, 9, 1, 2],
        [1, 2, 3, 1, 2, 3, 2, 1, 4, 3, 3]
    ]

    for lst in data:
        print(Counter(lst).most_common(1)[0][0])
        # or
        # print(max(lst, key=lst.count))


if __name__ == "__main__":
    main()
