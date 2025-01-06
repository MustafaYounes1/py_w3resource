"""

Write a Python program to remove specific words from a given list.

['red', 'green', 'blue', 'white', 'black', 'orange']
['white', 'orange']

['red', 'green', 'blue', 'black']

"""


def main():
    lst1 = ['red', 'green', 'blue', 'white', 'black', 'orange']
    lst2 = ['white', 'orange']

    print(list(filter(lambda _: _ not in lst2, lst1)))


if __name__ == "__main__":
    main()
