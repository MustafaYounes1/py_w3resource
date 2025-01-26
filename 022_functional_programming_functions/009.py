"""

Write a Python function that takes a number as a parameter and checks whether the number is prime or not.

9   =>  False
47  =>  True
89  =>  True
91  =>  False

"""

import math


def is_prime(n: int) -> bool:
    if n <= 1:
        return False

    for _ in range(2, int(math.sqrt(n)) + 1):
        if n % _ == 0:
            return False

    return True


def main():
    print(is_prime(9))
    print(is_prime(47))
    print(is_prime(89))
    print(is_prime(91))


if __name__ == "__main__":
    main()
