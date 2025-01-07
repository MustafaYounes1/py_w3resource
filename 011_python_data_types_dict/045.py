"""

Write a Python program to verify that all values in a dictionary are the same.

{'Cierra Vega': 12, 'Alden Cantrell': 12, 'Kierra Gentry': 12, 'Pierre Cox': 12}

all are 12  =>  True
all are 10  =>  False

"""


def main():
    data = {'Cierra Vega': 12, 'Alden Cantrell': 12, 'Kierra Gentry': 12, 'Pierre Cox': 12}
    vals = (12, 10)
    for v in vals:
        print(all(_ == v for _ in data.values()))


if __name__ == "__main__":
    main()
