"""

Write a Python program to extract numeric string elements and convert them to integers inside a given tuple using lambda

(('233', 'ABCD', '33'), ('1416', 'EFGH', '55'), ('2345', 'WERT', '34'))
((233, 33), (1416, 55), (2345, 34))

"""


def main():
    t = (('233', 'ABCD', '33'), ('1416', 'EFGH', '55'), ('2345', 'WERT', '34'))
    print(
        tuple(
            map(
                lambda st: tuple(map(int, st)),
                map(lambda st: filter(lambda __: __.isdigit(), st), t)
            )
        )
    )


if __name__ == "__main__":
    main()
