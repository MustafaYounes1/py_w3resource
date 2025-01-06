"""

Write a Python program to count the lowercase letters in a given list of words.

["Red", "Green", "Blue", "White"]       -> 13
["SQL", "C++", "C"]                     -> 0

"""


def main():
    data = [
        ["Red", "Green", "Blue", "White"],
        ["SQL", "C++", "C"]
    ]

    for lst in data:
        print(len(list(filter(lambda _: _.islower(), "".join(lst)))))


if __name__ == "__main__":
    main()
