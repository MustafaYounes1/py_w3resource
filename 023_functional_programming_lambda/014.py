"""

Write a Python program to filter a given list to determine if the values in the list have a length of 6 using Lambda.

['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']  =>  ['Monday', 'Friday', 'Sunday']

"""


def main():
    lst = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    print(list(filter(lambda _: len(_) == 6, lst)))


if __name__ == "__main__":
    main()
