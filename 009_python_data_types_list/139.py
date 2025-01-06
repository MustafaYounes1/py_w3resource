"""

Write a Python program to sort a given list of strings(numbers) numerically.

['4', '12', '45', '7', '0', '100', '200', '-12', '-500']

[-500, -12, 0, 4, 7, 12, 45, 100, 200]

"""


def main():
    lst = ['4', '12', '45', '7', '0', '100', '200', '-12', '-500']
    print(sorted(map(int, lst)))


if __name__ == "__main__":
    main()
