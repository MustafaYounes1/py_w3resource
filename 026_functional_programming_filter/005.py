"""

Write a Python function that filters out all empty strings from a list of strings using the filter function.

['', 'w3resource', 'Filter', '', 'Python', '']  =>  ['w3resource', 'Filter', 'Python']

"""


def main():
    lst = ['', 'w3resource', 'Filter', '', 'Python', '']
    print(list(filter(bool, lst)))


if __name__ == "__main__":
    main()
