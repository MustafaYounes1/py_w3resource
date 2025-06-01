"""

Write a Python program that performs common set operations like union, intersection, and difference of two frozensets.

[1, 2, 3, 4, 5], [0, 1, 3, 7, 8, 10]

Union:              {0, 1, 2, 3, 4, 5, 7, 8, 10}
Intersection:       {1, 3}
difference(a, b)    {2, 4, 5}
difference(b, a)    {0, 8, 10, 7}

"""


def main():
    s1, s2 = frozenset([1, 2, 3, 4, 5]), frozenset([0, 1, 3, 7, 8, 10])
    print(f"Union:              {s1 | s2}")
    print(f"Intersection:       {s1 & s2}")
    print(f"difference(a, b):   {s1 - s2}")
    print(f"difference(b, b):   {s2 - s1}")


if __name__ == "__main__":
    main()
