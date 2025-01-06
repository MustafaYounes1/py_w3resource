"""

Calculate the exponential of all elements in a list.

e.g.    lst = [1, 2, 3, 4, 5]

        [2.718281828459045, 7.38905609893065, 20.085536923187668, 54.598150033144236, 148.4131591025766]

"""

from math import exp


def main():
    lst = [1, 2, 3, 4, 5]
    print(list(map(exp, lst)))


if __name__ == "__main__":
    main()
