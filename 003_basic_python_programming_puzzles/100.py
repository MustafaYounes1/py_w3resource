"""

Write a Python program to find four positive even integers whose sum is a given integer.

n = 100         =>  [94, 2, 2, 2]
n = 1000        =>  [994, 2, 2, 2]
n = 10000       =>  [9994, 2, 2, 2]
n = 1234567890  =>  [1234567884, 2, 2, 2]

"""

import sys


def main():
    n = int(input("Enter a number: "))
    for a in range(n, 0, -1):
        # Skip odd values for a
        if not a % 2 == 0:
            continue

        # Iterate over possible values for the second even integer (b)
        for b in range(n - a, 0, -1):
            # Skip odd values for b
            if not b % 2 == 0:
                continue

            # Iterate over possible values for the third even integer (c)
            for c in range(n - b - a, 0, -1):
                # Skip odd values for c
                if not c % 2 == 0:
                    continue

                # Iterate over possible values for the fourth even integer (d)
                for d in range(n - b - c - a, 0, -1):
                    # Skip odd values for d
                    if not d % 2 == 0:
                        continue

                    # Check if the sum of a, b, c, and d equals the target number
                    if a + b + c + d == n:
                        # Return the list of found even integers
                        print([a, b, c, d])
                        sys.exit(0)


if __name__ == "__main__":
    main()
