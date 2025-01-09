"""

Write a Python program to get the total length of all values in a given dictionary with string values.

{'#FF0000': 'Red', '#800000': 'Maroon', '#FFFF00': 'Yellow', '#808000': 'Olive'}

20

"""


def main():
    d = {'#FF0000': 'Red', '#800000': 'Maroon', '#FFFF00': 'Yellow', '#808000': 'Olive'}
    print(sum(map(len, d.values())))


if __name__ == "__main__":
    main()
