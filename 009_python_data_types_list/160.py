"""

Remove the first 4 number of even numbers from the following list:

[3, 10, 4, 7, 5, 7, 8, 3, 3, 4, 5, 9, 3, 4, 9, 8, 5]

[3, 7, 5, 7, 3, 3, 5, 9, 3, 4, 9, 8, 5]

"""


def main():
    lst = [3, 10, 4, 7, 5, 7, 8, 3, 3, 4, 5, 9, 3, 4, 9, 8, 5]

    c = 0
    for _ in lst:
        if c == 4:
            break

        if _ % 2 == 0:
            lst.remove(_)
            c += 1

    print(lst)


if __name__ == "__main__":
    main()
