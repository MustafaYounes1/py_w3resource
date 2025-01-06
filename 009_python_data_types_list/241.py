"""

Write a Python program to create a dictionary with the unique values of a given list as keys and their frequencies
as values.


['a', 'b', 'f', 'a', 'c', 'e', 'a', 'a', 'b', 'e', 'f']     =>  {'a': 4, 'b': 2, 'f': 2, 'c': 1, 'e': 2}
[3, 4, 7, 5, 9, 3, 4, 5, 0, 3, 2, 3]                        =>  {3: 4, 4: 2, 7: 1, 5: 2, 9: 1, 0: 1, 2: 1}

"""

from collections import Counter


def main():
    data = [
        ['a', 'b', 'f', 'a', 'c', 'e', 'a', 'a', 'b', 'e', 'f'],
        [3, 4, 7, 5, 9, 3, 4, 5, 0, 3, 2, 3]
    ]

    for lst in data:
        print(dict(Counter(lst)))


if __name__ == "__main__":
    main()
