"""

Write a Python program to remove words from a given list of strings containing a character or string.

Original list:
list1: ['Red color', 'Orange#', 'Green', 'Orange @', 'White']

Character list:
['#', 'color', '@']

New list:
['Green', 'White']

"""


def main():
    lst1 = ['Red color', 'Orange#', 'Green', 'Orange @', 'White']
    lst2 = ['#', 'color', '@']

    print(list(filter(lambda _: not any(__ in _ for __ in lst2), lst1)))


if __name__ == "__main__":
    main()
