"""

Write a Python program that creates a list containing numbers from 1 to 10, but leaves a gap at even positions using
ellipsis.

[1, Ellipsis, 3, Ellipsis, 5, Ellipsis, 7, Ellipsis, 9, Ellipsis]

"""


def main():
    lst = [i if i % 2 else ... for idx, i in enumerate(range(1, 11))]
    print(lst)


if __name__ == "__main__":
    main()
