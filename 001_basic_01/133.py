"""

Write a Python program to calculate the time runs (difference between start and current time) of a program.

"""

import time


def loop():
    for _ in range(10):
        time.sleep(1)


def main():
    start = time.time()
    loop()
    end = time.time()

    print(f"Elapsed time: {end - start:.2f} sec")


if __name__ == "__main__":
    main()
