"""

Write a Python program to remove an element from a given list.

['Ricky Rivera', 98, 'Math', 90, 'Science']
Delete the first element    =>  [98, 'Math', 90, 'Science']

"""


def main():
    lst = ['Ricky Rivera', 98, 'Math', 90, 'Science']
    del lst[0]
    print(lst)


if __name__ == "__main__":
    main()
