"""

Sum a list of numbers. Write a Python program to sum the first number with the second and divide it by 2, then sum
the second with the third and divide by 2, and so on.

[1, 2, 3, 4, 5, 6, 7]
[1.5, 2.5, 3.5, 4.5, 5.5, 6.5]

[0, 1, -3, 3, 7, -5, 6, 7, 11]
[0.5, -1.0, 0.0, 5.0, 1.0, 0.5, 6.5, 9.0]

"""


def main():
    data = [
        [1, 2, 3, 4, 5, 6, 7],
        [0, 1, -3, 3, 7, -5, 6, 7, 11]
    ]

    for lst in data:
        print([(a + b) / 2 for a, b in zip(lst[:-1], lst[1:])])

if __name__ == "__main__":
    main()
