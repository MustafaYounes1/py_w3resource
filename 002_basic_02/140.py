"""

Write a Python program to convert all items in a given list to float values.

Original list:
[
'0.49', '0.54', '0.54', '0.54', '0.54', '0.54', '0.55', '0.54', '0.54', '0.54', '0.55', '0.55', '0.55', '0.54',
'0.55', '0.55', '0.54', '0.55', '0.55', '0.54'
]

List of Floats:
[0.49, 0.54, 0.54, 0.54, 0.54, 0.54, 0.55, 0.54, 0.54, 0.54, 0.55, 0.55, 0.55, 0.54, 0.55, 0.55, 0.54, 0.55, 0.55, 0.54]
"""


__sample_input = [
    '0.49', '0.54', '0.54', '0.54', '0.54', '0.54', '0.55', '0.54', '0.54', '0.54', '0.55', '0.55', '0.55', '0.54',
    '0.55', '0.55', '0.54', '0.55', '0.55', '0.54'
]


def main():
    print(list(map(float, __sample_input)))


if __name__ == "__main__":
    main()