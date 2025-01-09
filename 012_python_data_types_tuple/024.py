"""

Write a Python program to count the elements in a list until an element is a tuple.

[10, 20, 30, (10, 20), 40]  =>  3

"""


def main():
    lst = [10, 20, 30, (10, 20), 40]
    c = 0

    for _ in lst:
        if isinstance(_, tuple):
            break
        c += 1

    print(c)


if __name__ == "__main__":
    main()
