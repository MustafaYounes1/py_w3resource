"""

Find the second largest number in a list.

lst = [1, 2, 3, 4, 5]   =>  4

"""


def main():
    lst = [1, 2, 3, 4, 5]
    print(sorted(lst)[-2])


if __name__ == "__main__":
    main()
