"""

Write a Python program to find the largest number where commas or periods are decimal points.

Input:
['100', '102,1', '101.1']
Output:
102.1

"""


__data = ['100', '102,1', '101.1']


def main():
    print(
        max(list(map(lambda x: float(x.replace(",", ".")), __data)))
    )


if __name__ == "__main__":
    main()
