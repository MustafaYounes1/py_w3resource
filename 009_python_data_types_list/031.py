"""

Write a Python program to count the number of elements in a list within a specified range.

[10, 20, 30, 40, 40, 40, 70, 80, 99],   range(40, 100)      =>  6
['a', 'b', 'c', 'd', 'e', 'f'],         range('a', 'e')     =>  5

"""


def main():
    data = [
        ([10, 20, 30, 40, 40, 40, 70, 80, 99],   range(40, 100 + 1)),
        (['a', 'b', 'c', 'd', 'e', 'f'],         range(ord('a'), ord('e') + 1))
    ]

    for lst, r in data:
        if all(isinstance(_, int) for _ in lst):
            print(len([_ for _ in lst if _ in r]))

        elif all(isinstance(_, str) for _ in lst):
            print(len([_ for _ in lst if ord(_) in r]))

        else:
            raise TypeError("Supported types are: str and int")


if __name__ == "__main__":
    main()
