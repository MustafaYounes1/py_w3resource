"""

Write a Python program to remove additional spaces from a given list.

['abc ', ' ', ' ', 'sdfds ', ' ', ' ', 'sdfds ', 'huy']
['abc', '', '', 'sdfds', '', '', 'sdfds', 'huy']

"""


def main():
    lst = ['abc ', ' ', ' ', 'sdfds ', ' ', ' ', 'sdfds ', 'huy']
    print([_.strip() for _ in lst])


if __name__ == "__main__":
    main()
