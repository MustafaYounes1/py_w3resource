"""

Write a NumPy program to convert Fahrenheit degrees into Centigrade degrees (rounded to 2 decimal places).

Note:
    F = (C * 9/5) + 32
    C = (F - 32) * 5/9

[0, 12, 45.21, 34, 99.91, 32]       ->      [-17.78 -11.11   7.34   1.11  37.73   0.  ]


"""

import numpy as np


def main():
    f = [0, 12, 45.21, 34, 99.91, 32]
    c = (np.array(f) - 32) * 5/9
    print(np.round(c, 2))


if __name__ == "__main__":
    main()
