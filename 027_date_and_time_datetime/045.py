"""

Write a Python program to get the current week.

year: 2025, #week: 6, #weekday: 1

"""

from datetime import date


def main():
    y, w, wd = date.today().isocalendar()
    print(f"year: {y}, #week: {w}, #weekday: {wd}")


if __name__ == "__main__":
    main()
