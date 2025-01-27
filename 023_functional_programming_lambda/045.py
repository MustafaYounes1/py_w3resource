"""

Write a Python program to find the index position and value of the maximum and minimum values in a given list of
numbers using lambda.

[12, 33, 23, 10.11, 67, 89, 45, 66.7, 23, 12, 11, 10.25, 54]

(5, 89)
(3, 10.11)

"""


def main():
    lst = [12, 33, 23, 10.11, 67, 89, 45, 66.7, 23, 12, 11, 10.25, 54]
    print(max(enumerate(lst), key=lambda _: _[1]))
    print(min(enumerate(lst), key=lambda _: _[1]))


if __name__ == "__main__":
    main()
