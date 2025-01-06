"""

Generate a list of Fibonacci numbers up to a given number.

"""


def main():
    n = 100
    fibs = [0, 1]

    while fibs[-1] <= 100:
        fibs.append(fibs[-2] + fibs[-1])

    print(fibs[:-1])


if __name__ == "__main__":
    main()
