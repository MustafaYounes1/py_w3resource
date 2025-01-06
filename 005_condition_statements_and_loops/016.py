"""

Write a Python program to find numbers between 100 and 400 (both included) where each digit of a number is an even
number. The numbers obtained should be printed in a comma-separated sequence.

200,202,204,206,208,220,222,224,226,228,240,242,244,246,248,260,262,264,266,268,280,282,284,286,288,400

"""


def main():
    lst = [str(_) for _ in range(100, 401) if all(int(__) % 2 == 0 for __ in str(_))]
    print(", ".join(lst))


if __name__ == "__main__":
    main()
