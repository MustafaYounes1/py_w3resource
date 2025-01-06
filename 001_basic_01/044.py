"""

Write a Python program to locate Python site packages.

"""

import site


def main():
    # using site module
    # Return a list containing all global site-packages directories.
    # This can be useful for understanding where Python packages are installed on a particular system,
    # which can be important for managing dependencies in Python projects.
    print(site.getsitepackages())


if __name__ == "__main__":
    main()
