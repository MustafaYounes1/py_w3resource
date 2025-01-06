"""

Write a Python program to cast the provided value as a list if it's not one.

[1]                                 =>  <class 'list'>      [1]
('Red', 'Green')                    =>  <class 'tuple'>     ['Red', 'Green']
{'Red', 'Green'}                    =>  <class 'set'>       ['Green', 'Red']
{1: 'Red', 2: 'Green', 3: 'Black'}  =>  <class 'dict'>      [1, 2, 3]

"""


def main():
    data = [
        [1],
        ('Red', 'Green'),
        {'Red', 'Green'},
        {1: 'Red', 2: 'Green', 3: 'Black'}
    ]

    for el in data:
        print(type(el), list(el))


if __name__ == "__main__":
    main()
