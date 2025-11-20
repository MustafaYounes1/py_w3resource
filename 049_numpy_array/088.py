"""

Write a NumPy program to remove specific elements from a NumPy array.
Original array:
array([ 10,  20,  30,  40,  50,  60,  70,  80,  90, 100])

Delete first, fourth and fifth elements:
[ 20  30  60  70  80  90 100]

"""

import numpy as np


def main():
    a = np.arange(10, 110, 10)
    b = np.delete(a, [0, 3, 4])
    print(b)

if __name__ == "__main__":
    main()
