"""

Write a Python program to find the difference between two lists including duplicate elements.
Note: take the first list as your reference (it's the longer list)  "Left Difference"

[1, 1, 2, 3, 3, 4, 4, 5, 6, 7]
[1, 1, 2, 4, 5, 6]

[3, 3, 4, 7]

"""


def main():
    lst1 = [1, 1, 2, 3, 3, 4, 4, 5, 6, 7]
    lst2 = [1, 1, 2, 4, 5, 6]

    # copy the first list
    res = list(lst1)

    for _ in lst2:
        res.remove(_)

    print(res)


if __name__ == "__main__":
    main()
