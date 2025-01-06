"""

Invert a dictionary (swap keys and values).

d = {'a': 1, 'b': 2, 'c': 3}        =>  {1: 'a', 2: 'b', 3: 'c'}

"""


def main():
    d = {'a': 1, 'b': 2, 'c': 3}
    print(dict(zip(d.values(), d.keys())))


if __name__ == "__main__":
    main()
