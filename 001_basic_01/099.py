"""

Write a Python program to clear the screen or terminal.

"""

import os
import subprocess
import time


def main():
    print("Hello! this is a test (Would get erased from the terminal in 5 sec)")
    time.sleep(5)

    os.system("cls")

    time.sleep(2)

    print("Cleared with os.system! now trying the subprocess.call")
    time.sleep(5)

    subprocess.call(["cls"], shell=True)


if __name__ == "__main__":
    main()
