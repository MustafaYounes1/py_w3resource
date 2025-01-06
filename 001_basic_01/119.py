"""

Write a Python program to round a floating-point number to a specified number of decimal places.

round 212.374 with 2 decimal places

"""


def main():
    f = 212.374
    print(round(f, 2))
    print("%.2f" % f)
    print(f"{f:.2f}")


if __name__ == "__main__":
    main()
