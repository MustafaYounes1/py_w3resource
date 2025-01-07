"""

Write a Python program to filter a dictionary based on values.

{'Cierra Vega': 175, 'Alden Cantrell': 180, 'Kierra Gentry': 165, 'Pierre Cox': 190}
Marks greater than 170

{'Cierra Vega': 175, 'Alden Cantrell': 180, 'Pierre Cox': 190}

"""


def main():
    data = {'Cierra Vega': 175, 'Alden Cantrell': 180, 'Kierra Gentry': 165, 'Pierre Cox': 190}
    print({k: v for k, v in data.items() if v > 170})


if __name__ == "__main__":
    main()
