"""

Write a Python script to check whether a given key already exists in a dictionary.

{1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}

5   =>  True
9   =>  False

"""


def main():
    d = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
    keys = (5, 9)

    for k in keys:
        print(k in d)


if __name__ == "__main__":
    main()
