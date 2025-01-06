"""

Convert a list of numbers to a list of their decimal logarithms (logarithm base 10).

e.g.    lst = [1, 10, 100, 1000]    =>  [0.0, 1.0, 2.0, 3.0]

"""

import math


def main():
    lst = [1, 10, 100, 1000]
    print(list(map(math.log10, lst)))


if __name__ == "__main__":
    main()
