"""

Create a random 4x4 list where the values range in [0, 10] and then set the elements at the indices [0, 2] and [3, 1]
to NaN and finally replace all nan values with the mean of the list.

"""

from itertools import chain
from math import isnan
import random
from statistics import mean


def main():
    random.seed(0)
    lst = [[random.randint(0, 10) for _ in range(4)] for __ in range(4)]
    print(lst)
    lst[0][2] = float('nan')
    lst[3][1] = float('nan')
    m = mean(list(filter(lambda x: not isnan(x), chain.from_iterable(lst))))
    print(lst)
    print(
        [[m if isnan(_) else _ for _ in row] for row in lst]
    )


if __name__ == "__main__":
    main()
