"""

Write a Python program to separate and print the numbers and their position in a given string.

"The following example creates an ArrayList with a capacity of 50 elements. Four elements are then added to the
ArrayList and the ArrayList is trimmed accordingly."

50, index: 62

"""

import re


def main():
    s = ("The following example creates an ArrayList with a capacity of 50 elements. Four elements are then added to "
         "the ArrayList and the ArrayList is trimmed accordingly.")

    for _ in re.finditer(r"\d+", s):
        print(f"{_.group()}, index: {_.start()}")


if __name__ == "__main__":
    main()
