"""

Write a Python program to convert a tuple of string values to a tuple of integer values.

(('333', '33'), ('1416', '55'))

((333, 33), (1416, 55))

"""


def main():
    t = (('333', '33'), ('1416', '55'))
    print(tuple(tuple(map(int, _)) for _ in t))


if __name__ == "__main__":
    main()
