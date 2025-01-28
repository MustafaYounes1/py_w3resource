"""

Write a Python program that creates a list of names and uses the filter function to extract names that start with
a vowel (A, E, I, O, U).

['Elita', 'Vitold', 'Audovacar', 'Kerensa', 'Ramana', 'Iolanda', 'Landyn']  =>  ['Elita', 'Audovacar', 'Iolanda']

"""


def main():
    lst = ['Elita', 'Vitold', 'Audovacar', 'Kerensa', 'Ramana', 'Iolanda', 'Landyn']
    print(list(filter(lambda _: _[0] in "AEOIU", lst)))


if __name__ == "__main__":
    main()
