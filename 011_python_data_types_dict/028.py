"""

Write a Python program to sort the values (lists) in a dictionary.

num = {'n1': [2, 3, 1], 'n2': [5, 1, 2], 'n3': [3, 2, 4]}

{'n1': [1, 2, 3], 'n2': [1, 2, 5], 'n3': [2, 3, 4]}

"""


def main():
    num = {'n1': [2, 3, 1], 'n2': [5, 1, 2], 'n3': [3, 2, 4]}
    print({k: sorted(v) for k, v in num.items()})


if __name__ == "__main__":
    main()
