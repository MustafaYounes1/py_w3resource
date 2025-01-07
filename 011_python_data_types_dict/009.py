"""

Write a Python program to iterate over dictionaries using for loops.

d = {'Red': 1, 'Green': 2, 'Blue': 3}

Red      corresponds to  1
Green    corresponds to  2
Blue     corresponds to  3

"""


def main():
    d = {'Red': 1, 'Green': 2, 'Blue': 3}
    for k, v in d.items():
        print(f"{k:8} corresponds to {v:2}")


if __name__ == "__main__":
    main()
