"""

Write a Python program to create a flat list of all the keys in a flat dictionary.

{'Laura': 10, 'Spencer': 11, 'Bridget': 9, 'Howard ': 10}
['Laura', 'Spencer', 'Bridget', 'Howard ']

"""


def main():
    data = {'Laura': 10, 'Spencer': 11, 'Bridget': 9, 'Howard ': 10}
    print([_ for _ in data])


if __name__ == "__main__":
    main()
