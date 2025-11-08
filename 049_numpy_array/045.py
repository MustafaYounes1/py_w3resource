"""

Write a NumPy program to create a 1-D array of 20 elements spaced evenly on a log scale between 2. and 5., exclusive.

[  100.           141.25375446   199.5262315    281.83829313
   398.10717055   562.34132519   794.32823472  1122.0184543
  1584.89319246  2238.72113857  3162.27766017  4466.83592151
  6309.5734448   8912.50938134 12589.25411794 17782.79410039
 25118.8643151  35481.33892336 50118.72336273 70794.57843841]

"""

import numpy as np


def main():
    a = np.logspace(2,5,20, endpoint=False)

    log_diffs = np.diff(np.log10(a))    # ~ 0.15
    assert np.allclose(log_diffs[:-1], log_diffs[1:]), "value are expected to be evenly spaced on a log scale."

    print(a)


if __name__ == "__main__":
    main()
