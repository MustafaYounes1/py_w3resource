"""

Write a Python program to find the class wise roll number from a tuple-of-tuples.

classes = (
    ('V', 1),
    ('VI', 1),
    ('V', 2),
    ('VI', 2),
    ('VI', 3),
    ('VII', 1),
)

{'V': [1, 2], 'VI': [1, 2, 3], 'VII': [1]}

"""

from collections import defaultdict


def main():
    classes = (
        ('V', 1),
        ('VI', 1),
        ('V', 2),
        ('VI', 2),
        ('VI', 3),
        ('VII', 1),
    )

    d = defaultdict(list)

    for k, v in classes:
        d[k].append(v)

    print(dict(d))

if __name__ == "__main__":
    main()
