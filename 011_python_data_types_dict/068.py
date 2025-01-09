"""

Write a Python program to combine two or more dictionaries, creating a list of values for each key.

{'w': 50, 'x': 100, 'y': 'Green', 'z': 400}
{'x': 300, 'y': 'Red', 'z': 600}

{'w': [50], 'x': [100, 300], 'y': ['Green', 'Red'], 'z': [400, 600]}

"""

from collections import defaultdict


def main():
    data = [
        {'w': 50, 'x': 100, 'y': 'Green', 'z': 400},
        {'x': 300, 'y': 'Red', 'z': 600}

    ]

    out = defaultdict(list)
    for d in data:
        for k, v in d.items():
            out[k].append(v)

    print(dict(out))


if __name__ == "__main__":
    main()
