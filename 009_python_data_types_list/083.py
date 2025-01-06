"""

Write a Python program to round every number in a given list of numbers and print the total sum multiplied by the
length of the list.

[22.4, 4.0, -16.22, -9.1, 11.0, -12.22, 14.2, -5.2, 17.5]

243

"""


def main():
    lst = [22.4, 4.0, -16.22, -9.1, 11.0, -12.22, 14.2, -5.2, 17.5]
    print(sum(list(map(round, lst))) * len(lst))


if __name__ == "__main__":
    main()
