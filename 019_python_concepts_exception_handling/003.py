"""

Write a Python program that opens a file and handles a FileNotFoundError exception if the file does not exist.

"""

import random


def main():
    try:
        random.seed(0)
        random_fn = "".join(map(str, [random.randint(1, 10) for _ in range(20)])) + ".txt"
        with open(random_fn, 'r') as f:
            print(f.readlines())

    except FileNotFoundError as e:
        print(e)


if __name__ == "__main__":
    main()
