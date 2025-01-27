"""

Write a Python program to sort a list of dictionaries using Lambda.

Sort based on the 'color' key
[
    {'make': 'Nokia', 'model': 216, 'color': 'Black'},
    {'make': 'Mi Max', 'model': '2', 'color': 'Gold'},
    {'make': 'Samsung', 'model': 7, 'color': 'Blue'}
]

[
    {'make': 'Nokia', 'model': 216, 'color': 'Black'},
    {'make': 'Samsung', 'model': 7, 'color': 'Blue'},
    {'make': 'Mi Max', 'model': '2', 'color': 'Gold'}
]

"""


def main():
    lst = [
        {'make': 'Nokia', 'model': 216, 'color': 'Black'},
        {'make': 'Mi Max', 'model': '2', 'color': 'Gold'},
        {'make': 'Samsung', 'model': 7, 'color': 'Blue'}
    ]
    print(sorted(lst, key=lambda _: _.get("color")))


if __name__ == "__main__":
    main()
