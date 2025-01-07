"""

Write a Python program to filter the height and width of students, which are stored in a dictionary.

{'Cierra Vega': (6.2, 70), 'Alden Cantrell': (5.9, 65), 'Kierra Gentry': (6.0, 68), 'Pierre Cox': (5.8, 66)}
Height >= 6ft and Weight >= 70kg:

{'Cierra Vega': (6.2, 70)}

"""


def main():
    data = {'Cierra Vega': (6.2, 70), 'Alden Cantrell': (5.9, 65), 'Kierra Gentry': (6.0, 68), 'Pierre Cox': (5.8, 66)}
    print({k: v for k, v in data.items() if v[0] >= 6 and v[1] >= 70})


if __name__ == "__main__":
    main()
