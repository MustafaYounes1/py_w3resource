"""

Write a Python script to add a key to a dictionary.

{0: 10, 1: 20}
2: 30

=>  {0: 10, 1: 20, 2: 30}

"""


def main():
    d = {0: 10, 1: 20}
    d.setdefault(2, 30)
    print(d)


if __name__ == "__main__":
    main()
