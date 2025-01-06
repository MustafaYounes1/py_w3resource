"""

Write a Python program to find items that are parity outliers in a given list.
Note: The parity is oddness/evenness

[1, 2, 3, 4, 6]         =>  [1, 3]
[1, 2, 3, 4, 5, 6, 7]   =>  [2, 4, 6]

"""

from collections import Counter


def main():
    data = [
        [1, 2, 3, 4, 6],
        [1, 2, 3, 4, 5, 6, 7]
    ]

    for lst in data:
        most_common_parity = Counter(_ % 2 for _ in lst).most_common(n=1)[0][0]
        print([_ for _ in lst if _ % 2 != most_common_parity])


if __name__ == "__main__":
    main()
