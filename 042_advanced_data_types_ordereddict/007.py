"""

Write a Python function that merges two OrderedDict objects. If there are duplicate keys, sum their values. Print the
merged OrderedDict.

d1:
    ('Laptop', 40),
    ('Desktop', 45),
    ('Mobile', 35)

d2:
    ('Laptop', 40),
    ('Charger', 25)

OrderedDict([('Laptop', 80), ('Desktop', 45), ('Mobile', 35), ('Charger', 25)])

"""

from collections import defaultdict, OrderedDict


def main():
    d1 = OrderedDict([('Laptop', 40), ('Desktop', 45), ('Mobile', 35)])
    d2 = OrderedDict([('Laptop', 40), ('Charger', 25)])

    res = defaultdict(int)

    for d in (d1, d2):
        for k, v in d.items():
            res[k] += v

    res = OrderedDict(res)
    print(res)


if __name__ == "__main__":
    main()
