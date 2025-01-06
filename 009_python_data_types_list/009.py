"""

Write a Python program to clone or copy a list.

"""

from copy import deepcopy


def main():
    lst = [1, 2, 3]
    # or you can use
    # copied = list(lst)
    copied = deepcopy(lst)
    print(copied)


if __name__ == "__main__":
    main()
