"""

Write a Python program to convert all units of time into seconds.

"""


def main():
    time = input("Enter the time in the format: dd hh mm ss ")
    d, h, m, s = [int(_) for _ in time.split()]
    print(f"Time in second: {s + m * 60 + h * pow(60, 2) + d * 24 * pow(60, 2)}")


if __name__ == "__main__":
    main()
