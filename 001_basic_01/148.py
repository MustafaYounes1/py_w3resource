"""

Write a Python function to find the maximum and minimum numbers from a sequence of numbers.
Note: Do not use built-in functions.

"""


def main():
    seq = [int(_) for _ in input("Enter a list of space-separated integers: ").split()]

    mi, ma = seq[0], seq[1]
    for _ in seq:
        if _ < mi:
            mi = _
        if _ > ma:
            ma = _

    print(f"Min: {mi}, Max: {ma}")


if __name__ == "__main__":
    main()
