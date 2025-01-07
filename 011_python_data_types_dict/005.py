"""

Write a Python program to iterate over dictionaries using for loops.

d = {'x': 10, 'y': 20, 'z': 30}

x -> 10
y -> 20
z -> 30

"""


def main():
    d = {'x': 10, 'y': 20, 'z': 30}
    for k, v in d.items():
        print(f"{k} -> {v}")


if __name__ == "__main__":
    main()
