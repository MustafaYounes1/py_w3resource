"""

Create a 3x3 list of lists with random values ranging in [0, 100] and normalize it using the formula:
    Min-max scaling (z-score normalization): x' = (x -min) / (max -min)

"""

from random import randint, seed


def main():
    seed(0)
    lst = [
        [randint(0, 100) for _ in range(3)] for _ in range(3)
    ]
    print(f"The random list: {lst}")

    mi = min([min(_) for _ in lst])
    ma = max([max(_) for _ in lst])

    print(
        [[(_ - mi) / (ma - mi) for _ in __] for __ in lst]
    )


if __name__ == "__main__":
    main()
