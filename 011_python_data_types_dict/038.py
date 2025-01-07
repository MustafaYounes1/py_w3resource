"""

Write a Python program to match key values in two dictionaries.

{'key1': 1, 'key2': 3, 'key3': 2}, {'key1': 1, 'key2': 2}

key1: 1

"""


def main():
    d1, d2 = {'key1': 1, 'key2': 3, 'key3': 2}, {'key1': 1, 'key2': 2}
    print(set(d1.items()) & set(d2.items()))


if __name__ == "__main__":
    main()
