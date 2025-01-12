"""

Write a Python program to count the occurrences of each element in a given list.

['Green', 'Red', 'Blue', 'Red', 'Orange', 'Black', 'Black', 'White', 'Orange']
{'Green': 1, 'Red': 2, 'Blue': 1, 'Orange': 2, 'Black': 2, 'White': 1}

[3, 5, 0, 3, 9, 5, 8, 0, 3, 8, 5, 8, 3, 5, 8, 1, 0, 2]
{3: 4, 5: 4, 0: 3, 9: 1, 8: 4, 1: 1, 2: 1}

"""

from collections import Counter


def main():
    data = [
        ['Green', 'Red', 'Blue', 'Red', 'Orange', 'Black', 'Black', 'White', 'Orange'],
        [3, 5, 0, 3, 9, 5, 8, 0, 3, 8, 5, 8, 3, 5, 8, 1, 0, 2]
    ]

    for lst in data:
        print(dict(Counter(lst)))


if __name__ == "__main__":
    main()
