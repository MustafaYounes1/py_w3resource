"""

Write a Python program to calculate the maximum aggregate from the list of tuples (pairs).

[('Juan Whelan', 90), ('Sabah Colley', 88), ('Peter Nichols', 7), ('Juan Whelan', 122), ('Sabah Colley', 84)]

('Juan Whelan', 212)

"""

from collections import defaultdict
from operator import itemgetter


def main():
    lst = [('Juan Whelan', 90), ('Sabah Colley', 88), ('Peter Nichols', 7), ('Juan Whelan', 122), ('Sabah Colley', 84)]
    agg = defaultdict(lambda: 0)

    for k, v in lst:
        agg[k] += v

    print(max(agg.items(), key=itemgetter(1)))


if __name__ == "__main__":
    main()
