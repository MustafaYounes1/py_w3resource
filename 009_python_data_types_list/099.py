"""

Write a Python program to find the maximum and minimum values in a given heterogeneous list.

['Python', 3, 2, 4, 5, 'version']
(5, 2)

"""


def main():
    lst = ['Python', 3, 2, 4, 5, 'version']
    lst = list(filter(lambda _: isinstance(_, int), lst))
    print(max(lst), min(lst))


if __name__ == "__main__":
    main()
