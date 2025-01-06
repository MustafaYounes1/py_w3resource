"""

Convert radians to degrees for each element in a list.

lst = [pi / 2, pi, 3 * pi / 2]

[90.0, 180.0, 270.0]

"""

import math


def main():
    lst = [math.pi / 2, math.pi, 3 * math.pi / 2]
    print(list(map(math.degrees, lst)))


if __name__ == "__main__":
    main()
