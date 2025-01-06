"""

Write a Python program to add two objects if both objects are integers.

"""


def main():
    inputs = ((1, 4), (1.0, 2.0))
    for pair in inputs:
        if isinstance(pair[0], int) and isinstance(pair[1], int):
            print(pair[0] + pair[1])
        else:
            print("Expected two integers")


if __name__ == "__main__":
    main()
