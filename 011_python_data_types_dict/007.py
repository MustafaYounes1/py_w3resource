"""

Write a Python script to print a dictionary where the keys are numbers between 1 and 15 (both included) and the values
are the square of the keys.

{1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100, 11: 121, 12: 144, 13: 169, 14: 196, 15: 225}

"""


def main():
    keys = list(range(1, 16))
    print(dict(zip(keys, map(lambda _: pow(_, 2),keys))))


if __name__ == "__main__":
    main()
