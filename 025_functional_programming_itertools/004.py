"""

Write a Python program to construct an infinite iterator that returns evenly spaced values starting with a specified
number (10) and a step (1). Print the first 10 values

10 11 12 13 14 15 16 17 18 19

"""

from itertools import count


def main():
    itr = count(10, 1)
    for _ in range(10):
        print(next(itr), end=" ")


if __name__ == "__main__":
    main()
