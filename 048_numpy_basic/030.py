"""

Write a NumPy program to create a 3x3x3 array of int8 datatype, filled with arbitrary values.

[[[ 32   0  70]
  [  0 105   0]
  [108   0 101]]

 [[  0 115   0]
  [ 32   0  40]
  [  0 120   0]]

 [[ 56   0  54]
  [  0  41   0]
  [ 92   0  67]]]

Note: the above result may vary, and depends on what was found in the memory.

"""

import numpy as np


def main():
    a = np.empty((3, 3, 3), dtype=np.int8)
    print(a)


if __name__ == "__main__":
    main()
