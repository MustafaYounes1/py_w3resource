"""

Calculate the mean of each row in a 2D list ignoring nan values.

matrix = [[1, 2, NaN], [4, NaN, 6], [7, 8, 9]]

[1.5, 5.0, 8.0]

"""

import math
from statistics import mean


def main():
    matrix = [[1, 2, float('nan')], [4, float('nan'), 6], [7, 8, 9]]
    print([mean([_ for _ in row if not math.isnan(_)]) for row in matrix])


if __name__ == "__main__":
    main()
