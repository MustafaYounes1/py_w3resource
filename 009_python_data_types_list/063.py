"""

Write a Python program to insert a given string at the beginning of all items in a list.

[1,2,3,4], emp

['emp1', 'emp2', 'emp3', 'emp4']

"""


def main():
    lst, s = [1,2,3,4], 'emp'
    print([f"{s}{str(_)}" for _ in lst])


if __name__ == "__main__":
    main()
