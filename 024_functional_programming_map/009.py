"""

Write a Python program to create a new list taking specific elements from a tuple and convert a string value to an
integer.

[
    ('Alberto Franco','15/05/2002','35kg'),
    ('Gino Mcneill','17/05/2002','37kg'),
    ('Ryan Parkes','16/02/1999', '39kg'),
    ('Eesha Hinton','25/09/1998', '35kg')
]

['Alberto Franco', 'Gino Mcneill', 'Ryan Parkes', 'Eesha Hinton']
['15/05/2002', '17/05/2002', '16/02/1999', '25/09/1998']
[35, 37, 39, 35]

"""

from operator import itemgetter
from string import ascii_letters


def main():
    data = [
        ('Alberto Franco', '15/05/2002', '35kg'),
        ('Gino Mcneill', '17/05/2002', '37kg'),
        ('Ryan Parkes', '16/02/1999', '39kg'),
        ('Eesha Hinton', '25/09/1998', '35kg')
    ]

    print(list(map(itemgetter(0), data)))
    print(list(map(itemgetter(1), data)))
    print(list(map(lambda _: int(itemgetter(2)(_).translate(str.maketrans("", "", ascii_letters))), data)))


if __name__ == "__main__":
    main()
