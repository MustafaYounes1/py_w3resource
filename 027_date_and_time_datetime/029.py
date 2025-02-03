"""

Write a Python program to get GMT and the local time.

Local time: Mon, 03 February 2025 16:33:39 PM
GMT time:   Mon, 03 February 2025 13:33:39 PM

"""

from time import gmtime, localtime, strftime


def main():
    print(f"Local time: {strftime('%a, %d %B %Y %H:%M:%S %p', localtime())}")
    print(f"GMT time:   {strftime('%a, %d %B %Y %H:%M:%S %p', gmtime())}")


if __name__ == "__main__":
    main()
