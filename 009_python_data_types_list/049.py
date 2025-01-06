"""

Write a Python program to convert a list to a list of dictionaries.

["Black", "Red", "Maroon", "Yellow"], ["#000000", "#FF0000", "#800000", "#FFFF00"]
[
{'color_name': 'Black', 'color_code': '#000000'},
{'color_name': 'Red', 'color_code': '#FF0000'},
{'color_name': 'Maroon', 'color_code': '#800000'},
{'color_name': 'Yellow', 'color_code': '#FFFF00'}]

"""


def main():
    names, vals = ["Black", "Red", "Maroon", "Yellow"], ["#000000", "#FF0000", "#800000", "#FFFF00"]
    print(
        [{'color_name': n, 'color_code': v} for n, v in zip(names, vals)]
    )


if __name__ == "__main__":
    main()
