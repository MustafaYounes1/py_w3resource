"""

Write a Numpy program to get the Numpy version and show the Numpy build configuration.

"""

import numpy as np


def main():
    print(f"NumPy version: {np.version.version}")
    print(np.show_config('dicts'))  # Show libraries and system information on which NumPy was built and is being used


if __name__ == "__main__":
    main()
