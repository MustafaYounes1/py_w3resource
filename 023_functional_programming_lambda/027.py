"""

Write a Python program to sort each sublist of strings in a given list of lists using lambda.

[['green', 'orange'], ['black', 'white'], ['white', 'black', 'orange']]
[['green', 'orange'], ['black', 'white'], ['black', 'orange', 'white']]

"""


def main():
    lst = [['green', 'orange'], ['black', 'white'], ['white', 'black', 'orange']]
    print(list(map(lambda _: sorted(_), lst)))


if __name__ == "__main__":
    main()
