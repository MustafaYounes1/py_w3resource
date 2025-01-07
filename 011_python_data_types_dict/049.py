"""

Write a Python program to convert string values of a given dictionary into integer datatypes.

[{'x': '10', 'y': '20', 'z': '30'}, {'p': '40', 'q': '50', 'r': '60'}]
[{'x': 10, 'y': 20, 'z': 30}, {'p': 40, 'q': 50, 'r': 60}]

"""


def main():
    data = [{'x': '10', 'y': '20', 'z': '30'}, {'p': '40', 'q': '50', 'r': '60'}]
    print([{k: int(v) for k, v in d.items()} for d in data])


if __name__ == "__main__":
    main()
