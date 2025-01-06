"""

Write a Python program to randomly generate a list of 10 even numbers between 1 and 100 inclusive.

Note: Use random.sample() to generate a list of random values.
Sample Input:   (1,100)
Sample Output:  [4, 22, 8, 20, 24, 12, 30, 98, 28, 48]

"""

import random


def main():
    print(random.sample([_ for _ in range(1, 101) if _ % 2 == 0], 10))


if __name__ == "__main__":
    main()
