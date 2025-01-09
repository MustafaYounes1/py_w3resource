"""

Write a Python program to combine two lists into a dictionary. The elements of the first one serve as keys and the
elements of the second one serve as values. Each item in the first list must be unique and hashable.

['a', 'b', 'c', 'd', 'e', 'f']
[1, 2, 3, 4, 5]

{'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}

"""


def main():
    lst1 = ['a', 'b', 'c', 'd', 'e', 'f']
    lst2 = [1, 2, 3, 4, 5]
    print(dict(zip(lst1, lst2)))


if __name__ == "__main__":
    main()
