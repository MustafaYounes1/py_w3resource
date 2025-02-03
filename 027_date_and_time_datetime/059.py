"""

Write a Python program that takes a tuple containing 9 elements corresponding to structure time as an argument and
returns a string representing it.

(2020, 1, 22, 2, 34, 6, 6, 362, 0)  =>  Sun Jan 22 02:34:06 2020


"""

import time


def main():
    print(time.asctime((2020, 1, 22, 2, 34, 6, 6, 362, 0)))


if __name__ == "__main__":
    main()
