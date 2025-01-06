"""

Write a Python program to sort a given positive number in descending/ascending order.
Descending -> Highest to lowest.
Ascending -> Lowest to highest

Original Number: 134543
Descending order of the said number: 544331
Ascending order of the said number: 133445

Original Number: 43750973
Descending order of the said number: 97754330
Ascending order of the said number: 3345779

"""


def main():
    data = [
        134543,
        43750973
    ]

    for n in data:
        print(int("".join(sorted(list(str(n)), reverse=True))))
        print(int("".join(sorted(list(str(n)), reverse=False))))
        print('*' * 25)


if __name__ == "__main__":
    main()
