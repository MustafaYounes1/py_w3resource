"""

Write a Python program to group the elements of a given list based on the given function.

[7, 23, 3.2, 3.3, 8.4], floor
{7: [7], 23: [23], 3: [3.2, 3.3], 8: [8.4]}

['Red', 'Green', 'Black', 'White', 'Pink'], len
{3: ['Red'], 5: ['Green', 'Black', 'White'], 4: ['Pink']}

"""

from collections import defaultdict
from math import floor


def main():
    data = [
        [[7, 23, 3.2, 3.3, 8.4], floor],
        [['Red', 'Green', 'Black', 'White', 'Pink'], len]
    ]

    for lst, func in data:
        out = defaultdict(list)

        for _ in lst:
            out[func(_)].append(_)

        print(dict(out))



if __name__ == "__main__":
    main()
