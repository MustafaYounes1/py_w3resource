"""

Write a Python program that can suspend execution of a given script for a given number of seconds.

Sorry, Slept for 3 seconds...
Sorry, Slept for 3 seconds...
Sorry, Slept for 3 seconds...
Sorry, Slept for 3 seconds...

"""

import time


def main():
    for _ in range(4):
        time.sleep(3)
        print("Sorry, Slept for 3 seconds...")


if __name__ == "__main__":
    main()
