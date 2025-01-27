"""

Write a Python program to calculate the average value of the numbers in a given tuple of tuples using lambda.
    average all first numbers together
    average all second numbers together
    ...

((10, 10, 10), (30, 45, 56), (81, 80, 39), (1, 2, 3))       =>  (30.5, 34.25, 27.0)
((1, 1, -5), (30, -15, 56), (81, -60, -39), (-10, 2, 3))    =>  (25.5, -18.0, 3.75)

"""


def main():
    data = [
        ((10, 10, 10), (30, 45, 56), (81, 80, 39), (1, 2, 3)),
        ((1, 1, -5), (30, -15, 56), (81, -60, -39), (-10, 2, 3))
    ]

    for lst in data:
        print(list(map(lambda _: round(sum(_) / len(_), 2), zip(*lst))))


if __name__ == "__main__":
    main()
