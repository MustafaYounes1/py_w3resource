"""

Write a Python program to transform a dictionary into a list of tuples.

{'Red': 1, 'Green': 3, 'White': 5, 'Black': 2, 'Pink': 4}
[('Red', 1), ('Green', 3), ('White', 5), ('Black', 2), ('Pink', 4)]

"""


def main():
    d = {'Red': 1, 'Green': 3, 'White': 5, 'Black': 2, 'Pink': 4}
    print(list(d.items()))


if __name__ == "__main__":
    main()
