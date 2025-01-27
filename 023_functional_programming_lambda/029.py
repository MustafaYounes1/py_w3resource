"""

Write a Python program to find the maximum int value in a given heterogeneous list using lambda.

['Python', 3, 2, 4, 5, 'version']   =>  5

"""


def main():
    lst = ['Python', 3, 2, 4, 5, 'version']
    print(max(lst, key=lambda _: (isinstance(_, int), _)))


if __name__ == "__main__":
    main()
