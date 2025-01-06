"""

Write a Python program that converts seconds into days, hours, minutes, and seconds.

"""


def convert(s):
    mm, ss = divmod(s, 60)
    hh, mm = divmod(mm, 60)
    dd, hh = divmod(hh, 24)
    return dd, hh, mm, ss


def main():
    sec = int(input("Enter the time in seconds: "))
    d, h, m, s = convert(sec)
    print(f"Days: %i, Hours: %i, Minutes: %i, Seconds: %i" % (d, h, m, s))


if __name__ == "__main__":
    main()
