"""

rite a Python program to filter the height and width of students, which are stored in a dictionary using lambda.
    Height>= 6ft and Weight>= 70kg

{'Cierra Vega': (6.2, 70), 'Alden Cantrell': (5.9, 65), 'Kierra Gentry': (6.0, 68), 'Pierre Cox': (5.8, 66)}
{'Cierra Vega': (6.2, 70)}

"""


def main():
    d = {'Cierra Vega': (6.2, 70), 'Alden Cantrell': (5.9, 65), 'Kierra Gentry': (6.0, 68), 'Pierre Cox': (5.8, 66)}
    valid_items = list(filter(lambda _: _[1][0] >= 6 and _[1][1] >= 70, d.items()))
    print(dict(valid_items))


if __name__ == "__main__":
    main()
