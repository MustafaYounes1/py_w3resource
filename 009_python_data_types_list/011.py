"""

Write a Python function that takes two lists and returns True if they have at least one common member.

[1, 2, 3, 4, 5], [5, 6, 7, 8, 9]    =>  True
[1, 2, 3, 4, 5], [6, 7, 8, 9]       =>  False

"""


def main():
    lst1, lst2 = [1, 2, 3, 4, 5], [6, 7, 8, 9]
    print(len(set(lst1) & set(lst2)) > 0)


if __name__ == "__main__":
    main()
