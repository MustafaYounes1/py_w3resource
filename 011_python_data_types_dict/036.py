"""

Write a Python program to create a dictionary from two lists.

['Class-V', 'Class-VI', 'Class-VII', 'Class-VIII'], [1, 2, 2, 3]

{'Class-V': {1}, 'Class-VI': {2}, 'Class-VII': {2}, 'Class-VIII': {3}}

"""


def main():
    lst1, lst2 = ['Class-V', 'Class-VI', 'Class-VII', 'Class-VIII'], [1, 2, 2, 3]
    print(dict(zip(lst1, map(lambda _: set([_]), lst2))))


if __name__ == "__main__":
    main()
