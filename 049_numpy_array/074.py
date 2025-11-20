"""

Write a NumPy program to create an array of three column types (integer, floating, and character).

[(1, 2., b'Albert Einstein') (2, 2., b'Edmond Halley')
 (3, 3., b'Gertrude B. Elion')]

"""

import numpy as np


def main():
    a = np.array(
        [(1, 2., b'Albert Einstein'), (2, 2., b'Edmond Halley'), (3, 3., b'Gertrude B. Elion')],
        dtype="i8, f8, S25"
    )
    print(a)


if __name__ == "__main__":
    main()
