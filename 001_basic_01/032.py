"""

Write a Python program to find the least common multiple (LCM) of two positive integers.

"""

import math


# or from scratch
def lcm(x, y):
    # Compare 'x' and 'y' to determine the larger number and store it in 'z'.
    if x > y:
        z = x
    else:
        z = y

    # Use a 'while' loop to find the LCM.
    while True:
        # Check if 'z' is divisible by both 'x' and 'y' with no remainder.
        if (z % x == 0) and (z % y == 0):
            # If both conditions are met, 'z' is the LCM, so store it in 'lcm' and break the loop.
            res = z
            break
        # If the conditions are not met, increment 'z' and continue checking.
        z += 1

    # Return the calculated LCM.
    return res


def main():
    n1, n2 = [int(_) for _ in input("Enter the two numbers (space-separated): ").split()]
    print(f"LCM: {math.lcm(n1, n2)}")


if __name__ == "__main__":
    main()
