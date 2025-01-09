"""

Write a Python program to check whether an element exists within a tuple.

("w", 3, "r", "e", "s", "o", "u", "r", "c", "e")

'r' =>  True
5   =>  False

"""


def main():
    t = ("w", 3, "r", "e", "s", "o", "u", "r", "c", "e")
    print(list(map(lambda _: _ in t, ('r', 5))))


if __name__ == "__main__":
    main()
