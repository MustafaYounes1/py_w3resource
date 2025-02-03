"""

Write a Python program to display the date and time in a human-friendly string.

Monday, February 03, 2025, 05:03 PM

"""

from datetime import datetime


def main():
    print(datetime.now().strftime("%A, %B %d, %Y, %I:%M %p"))


if __name__ == "__main__":
    main()
