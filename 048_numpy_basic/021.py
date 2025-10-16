"""

Write a NumPy program to create a vector of length 10 with values evenly distributed between 5 and 50.

[ 5. 10. 15. 20. 25. 30. 35. 40. 45. 50.]

"""

import numpy as np


def main():
    a = np.linspace(5, 50, 10)
    print(a)


if __name__ == "__main__":
    main()
