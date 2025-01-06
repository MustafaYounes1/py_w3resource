"""

Write a Python program to check whether two lists are circularly identical.

[10, 10, 0, 0, 10], [10, 10, 10, 0, 0]  =>  True
[10, 10, 0, 0, 10], [1, 10, 10, 0, 0]   =>  False

"""


def main():
    lst1, lst2 = [10, 10, 0, 0, 10], [1, 10, 10, 0, 0]
    print(" ".join(list(map(str, lst2))) in " ".join(list(map(str, lst1 * 2))))


if __name__ == "__main__":
    main()
