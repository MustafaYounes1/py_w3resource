"""

Write a Python program to remove specific words from a given list using lambda.

['orange', 'red', 'green', 'blue', 'white', 'black']

Remove words:
['orange', 'black']

['red', 'green', 'blue', 'white']

"""


def main():
    lst1 = ['orange', 'red', 'green', 'blue', 'white', 'black']
    lst2 = ['orange', 'black']
    print(list(filter(lambda _: _ not in lst2, lst1)))


if __name__ == "__main__":
    main()
