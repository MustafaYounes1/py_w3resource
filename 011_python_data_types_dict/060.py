"""

Write a Python program to find the shortest list of values for the keys in a given dictionary.

{'V': [10, 12], 'VI': [10], 'VII': [10, 20, 30, 40], 'VIII': [20], 'IX': [10, 30, 50, 70], 'X': [80]}

['VI', 'VIII', 'X']

"""


def main():
    d = {'V': [10, 12], 'VI': [10], 'VII': [10, 20, 30, 40], 'VIII': [20], 'IX': [10, 30, 50, 70], 'X': [80]}
    min_l = min(map(len, d.values()))
    print(list(filter(lambda _: len(d.get(_)) == min_l, d)))


if __name__ == "__main__":
    main()
