"""

Write a Python program to generate and print a list of numbers from 1 to 10.

Sample Input:
range(1,10)

Sample Output:
[1, 2, 3, 4, 5, 6, 7, 8, 9]
['1', '2', '3', '4', '5', '6', '7', '8', '9']

"""


def main():
    inp = range(1, 10)
    print(list(inp))
    print(list(map(str, inp)))


if __name__ == "__main__":
    main()
