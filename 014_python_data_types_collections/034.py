"""

Write a Python program to create an instance of an OrderedDict using a given dictionary. Sort the dictionary during
the creation and print the members of the dictionary in reverse order.

{'Afghanistan': 93, 'Albania': 355, 'Algeria': 213, 'Andorra': 376, 'Angola': 244}

Angola 244
Andorra 376
Algeria 213
Albania 355
Afghanistan 93

"""

from collections import OrderedDict


def main():
    d_source = {'Afghanistan': 93, 'Albania': 355, 'Algeria': 213, 'Andorra': 376, 'Angola': 244}

    d_sorted = OrderedDict(
        {k: d_source[k] for k in sorted(d_source)}
    )

    for k in sorted(d_sorted, reverse=True):
        print(k, d_sorted[k])


if __name__ == "__main__":
    main()
