"""

Write a Python program to group the elements of a list based on the given function and return the count of elements
in each group.

[6.1, 4.2, 6.3], floor          =>  {6: 2, 4: 1}
['one', 'two', 'three'], len    =>  {3: 2, 5: 1}

"""

from collections import Counter
from math import floor


def main():
    print(dict(Counter(map(floor, [6.1, 4.2, 6.3]))))
    print(dict(Counter(map(len, ['one', 'two', 'three']))))


if __name__ == "__main__":
    main()
