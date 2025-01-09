"""

Write a Python program to get the depth of a dictionary.

{'a': 1, 'c': {1: 1, 2: {}}, 'b': {'c': {'d': {}}}}
4

"""


def find_depth(d):
    if isinstance(d, dict):
        return 1 + (max(map(find_depth, d.values())) if d else 0)
    else:
        return 0


def main():
    d = {'a': 1, 'c': {1: 1, 2: {}}, 'b': {'c': {'d': {}}}}
    print(find_depth(d))


if __name__ == "__main__":
    main()
