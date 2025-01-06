"""

Write a Python program to append a list to the second list.

[1, 2, 3, 0], ['Red', 'Green', 'Black']     =>  [1, 2, 3, 0, 'Red', 'Green', 'Black']

"""


def main():
    lst1, lst2 = [1, 2, 3, 0], ['Red', 'Green', 'Black']
    print(lst1 + lst2)


if __name__ == "__main__":
    main()
