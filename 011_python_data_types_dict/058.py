"""

Write a Python program to get all combinations of key-value pairs in a given dictionary.

{'V': [1, 4, 6, 10], 'VI': [1, 4, 12], 'VII': [1, 3, 8]}
[
    {'V': [1, 4, 6, 10], 'VI': [1, 4, 12]},
    {'V': [1, 4, 6, 10], 'VII': [1, 3, 8]},
    {'VI': [1, 4, 12], 'VII': [1, 3, 8]}
]

{'V': [1, 3, 5], 'VI': [1, 5]}
[
    {'V': [1, 3, 5], 'VI': [1, 5]}
]

"""

from itertools import combinations


def main():
    data = [
        {'V': [1, 4, 6, 10], 'VI': [1, 4, 12], 'VII': [1, 3, 8]},
        {'V': [1, 3, 5], 'VI': [1, 5]}
    ]

    for d in data:
        print(
            [dict(_) for _ in combinations(d.items(), 2)]
        )


if __name__ == "__main__":
    main()
