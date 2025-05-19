"""

Write a Python function that takes two boolean values as input and returns the logical AND and OR of those values.

False AND False = False
False OR  False = False
False AND True = False
False OR  True = True
True AND False = False
True OR  False = True
True AND True = True
True OR  True = True

"""

from itertools import product


def main():
    for a, b in product([False, True], [False, True]):
        print(f"{a} AND {b} = {a and b}")
        print(f"{a} OR  {b} = {a or b}")


if __name__ == "__main__":
    main()
