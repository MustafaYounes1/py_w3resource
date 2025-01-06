"""

Write a Python program to extract a single key-value pair from a dictionary into variables.

"""


def main():
    d = {
        "k1": "v1",
        "k2": "v2",
    }

    (k, v), _ = d.items()
    print(f"Key: {k}, value: {v}")


if __name__ == "__main__":
    main()
