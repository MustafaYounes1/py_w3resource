"""

Write a Python program to filter even numbers from a dictionary of values.

{'V': [1, 4, 6, 10], 'VI': [1, 4, 12], 'VII': [1, 3, 8]}
{'V': [4, 6, 10], 'VI': [4, 12], 'VII': [8]}

{'V': [1, 3, 5], 'VI': [1, 5], 'VII': [2, 7, 9]}
{'V': [], 'VI': [], 'VII': [2]}

"""


def main():
    data = [
        {'V': [1, 4, 6, 10], 'VI': [1, 4, 12], 'VII': [1, 3, 8]},
        {'V': [1, 3, 5], 'VI': [1, 5], 'VII': [2, 7, 9]}
    ]

    for d in data:
        print({k: [_ for _ in v if _ % 2 == 0] for k, v in d.items()})


if __name__ == "__main__":
    main()
