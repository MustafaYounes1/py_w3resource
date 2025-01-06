"""

Write a Python program to extend a list without appending.
insert the elements of 'y' at the beginning of 'x'

[10, 20, 30]
[40, 50, 60]

[40, 50, 60, 10, 20, 30]

"""


def main():
    lst1 = [10, 20, 30]
    lst2 = [40, 50, 60]
    lst1[:0] = lst2
    print(lst1)


if __name__ == "__main__":
    main()
