"""

Write a Python script to generate and print a dictionary that contains a number (between 1 and n) in the form (x, x*x).

n = 5

{1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

"""


def main():
    n = 5
    keys = list(range(1, n+1))
    print(dict(zip(keys, map(lambda _: pow(_, 2), keys))))


if __name__ == "__main__":
    main()
