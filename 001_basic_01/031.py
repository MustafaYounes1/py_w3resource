"""

Write a Python program that computes the greatest common divisor (GCD) of two positive integers.

"""

import math


# or from scratch
def gcd(x, y):
    # Initialize gcd to 1.
    res = 1

    # Check if y is a divisor of x (x is divisible by y).
    if x % y == 0:
        return y

    # Iterate from half of y down to 1.
    for k in range(int(y / 2), 0, -1):
        # Check if both x and y are divisible by k.
        if x % k == 0 and y % k == 0:
            # Update the GCD to the current value of k and exit the loop.
            res = k
            break

    # Return the calculated GCD.
    return res


def main():
    n1, n2 = [int(_) for _ in input("Enter the two integers: (space-separated) ").split()]
    print(f"GCD: {math.gcd(n1, n2)}")


if __name__ == "__main__":
    main()
