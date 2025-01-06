"""

Check if a number is prime.

1   =>  False
17  =>  True

"""

import math


def is_prime(n):
    if n == 1:
        return False

    for _ in range(2, int(math.sqrt(n)) + 1):
        if n % _ == 0:
            return False

    return True


def main():
    n = 17
    print(is_prime(n))


if __name__ == "__main__":
    main()
