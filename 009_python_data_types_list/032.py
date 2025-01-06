"""

Write a Python program to check whether a list contains a sublist.

[2, 4, 3, 5, 7], [4, 3]     =>  True
[2, 4, 3, 5, 7], [3, 7]     =>  False

"""


def main():
    data = [
        [[2, 4, 3, 5, 7], [4, 3]],
        [[2, 4, 3, 5, 7], [3, 7]]
    ]

    for lst1, lst2 in data:
        print(" ".join(list(map(str, lst2))) in " ".join(list(map(str, lst1))))


if __name__ == "__main__":
    main()
