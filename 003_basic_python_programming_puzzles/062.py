"""

Write a Python program to find the dictionary key whose case is different from all other keys.

{'red': '', 'GREEN': '', 'blue': 'orange'}      =>  GREEN
{'RED': '', 'GREEN': '', 'orange': '#125GD'}    =>  orange

"""

__data = [
    {'red': '', 'GREEN': '', 'blue': 'orange'},
    {'RED': '', 'GREEN': '', 'orange': '#125GD'}
]


def main():
    for sample in __data:
        keys = list(sample.keys())
        cases = ["lower" if _.islower() else "upper" for _ in keys]
        lowers_count = cases.count("lower")
        print(
            keys[cases.index("lower") if lowers_count == 1 else cases.index("upper")]
        )


if __name__ == "__main__":
    main()
