"""

Write a Python program to print a string five times, with a delay of three seconds..

"""

import time


def main():
    for _ in range(5):
        time.sleep(5)
        print("Hello world!")


if __name__ == "__main__":
    main()
