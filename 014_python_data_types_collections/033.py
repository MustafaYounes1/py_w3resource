"""

Write a Python program to count the number of students in an individual class.
Note: if a class was repeated, the latest number should be considered

classes = (
    ('V', 1),
    ('VI', 1),
    ('V', 2),
    ('VI', 2),
    ('VI', 3),
    ('VII', 1),
)

{'V': 2, 'VI': 3, 'VII': 1}

"""

from collections import Counter


def main():
    classes = (
        ('V', 1),
        ('VI', 1),
        ('V', 2),
        ('VI', 2),
        ('VI', 3),
        ('VII', 1),
    )

    c = Counter(
        {k: v for k, v in classes}
    )

    print(dict(c))


if __name__ == "__main__":
    main()
