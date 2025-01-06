"""

Write a Python program to split a list into different variables.

color = [
    ("Black", "#000000", "rgb(0, 0, 0)"),
    ("Red", "#FF0000", "rgb(255, 0, 0)"),
    ("Yellow", "#FFFF00", "rgb(255, 255, 0)")
]

Black #000000 rgb(0, 0, 0)
Red #FF0000 rgb(255, 0, 0)
Yellow #FFFF00 rgb(255, 255, 0)

"""


def main():
    color = [
        ("Black", "#000000", "rgb(0, 0, 0)"),
        ("Red", "#FF0000", "rgb(255, 0, 0)"),
        ("Yellow", "#FFFF00", "rgb(255, 255, 0)")
    ]

    for c_str, c_hex, c_rgb in color:
        print(c_str, c_hex, c_rgb)


if __name__ == "__main__":
    main()
