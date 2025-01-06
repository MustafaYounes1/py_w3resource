"""

Describe the Write a Python program to remove a specific item at a specific column from a given list of lists.

[
    ['Red', 'Maroon', 'Yellow', 'Olive'],
    ['#FF0000', '#800000', '#FFFF00', '#808000'],
    ['rgb(255,0,0)', 'rgb(128,0,0)', 'rgb(255,255,0)', 'rgb(128,128,0)']
]

Remove 1st list from the saod given list of lists:
[
    ['Maroon', 'Yellow', 'Olive'],
    ['#800000', '#FFFF00', '#808000'],
    ['rgb(128,0,0)', 'rgb(255,255,0)', 'rgb(128,128,0)']
]

Remove 2nd list from the saod given list of lists:
[
    ['Red', 'Yellow', 'Olive'],
    ['#FF0000', '#FFFF00', '#808000'],
    ['rgb(255,0,0)', 'rgb(255,255,0)', 'rgb(128,128,0)']
]

Remove 4th list from the saod given list of lists:
[
    ['Red', 'Maroon', 'Yellow'],
    ['#FF0000', '#800000', '#FFFF00'],
    ['rgb(255,0,0)', 'rgb(128,0,0)', 'rgb(255,255,0)']
]

"""


def main():
    data = [
        ['Red', 'Maroon', 'Yellow', 'Olive'],
        ['#FF0000', '#800000', '#FFFF00', '#808000'],
        ['rgb(255,0,0)', 'rgb(128,0,0)', 'rgb(255,255,0)', 'rgb(128,128,0)']
    ]

    for c in (1, 2, 4):
        print(
            [[__ for idx, __ in enumerate(_) if idx != c - 1] for _ in data]
        )


if __name__ == "__main__":
    main()
