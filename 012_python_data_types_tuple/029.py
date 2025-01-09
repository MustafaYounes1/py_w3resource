"""

Write a Python program to convert a given tuple of positive integers into an integer.

(1, 2, 3)           =>  123
(10, 20, 40, 5, 70) =>  102040570

"""


def main():
    data = [
        (1, 2, 3),
        (10, 20, 40, 5, 70)
    ]

    for _ in data:
        print(int("".join(map(str, _))))


if __name__ == "__main__":
    main()
