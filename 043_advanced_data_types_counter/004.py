"""

Write a Python program that creates two 'Counter' objects and finds their sum, difference, union, and intersection.

ctr1 = Counter(x=3, y=2, z=10)
ctr2 = Counter(x=1, y=2, z=3)

Sum:            Counter({'z': 13, 'x': 4, 'y': 4})
Difference:     Counter({'z': 7, 'x': 2})
Union:          Counter({'z': 10, 'x': 3, 'y': 2})
Intersection:   Counter({'z': 3, 'y': 2, 'x': 1})

"""

from collections import Counter


def main():
    ctr1 = Counter(x=3, y=2, z=10)
    ctr2 = Counter(x=1, y=2, z=3)

    # if a key is missed in one of them -> it would be zero in the other one
    print(f"Sum:            {ctr1 + ctr2}")  # sums the counts
    print(f"Difference:     {ctr1 - ctr2}")  # subtracts the counts and omits the zero/negative ones (subtract method keeps them)
    print(f"Union:          {ctr1 | ctr2}")  # maximum count
    print(f"Intersection:   {ctr1 & ctr2}")  # minimum count


if __name__ == "__main__":
    main()
