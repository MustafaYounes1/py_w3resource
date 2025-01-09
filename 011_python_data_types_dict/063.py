"""

Write a Python program to convert a given list of lists to a dictionary.
Note: Consider the first element of each list as a key in the output dict

[
    [1, 'Jean Castro', 'V'],
    [2, 'Lula Powell', 'V'],
    [3, 'Brian Howell', 'VI'],
    [4, 'Lynne Foster', 'VI'],
    [5, 'Zachary Simon', 'VII']
]

{
    1: ['Jean Castro', 'V'],
    2: ['Lula Powell', 'V'],
    3: ['Brian Howell', 'VI'],
    4: ['Lynne Foster', 'VI'],
    5: ['Zachary Simon', 'VII']
}

"""


def main():
    data = [
        [1, 'Jean Castro', 'V'],
        [2, 'Lula Powell', 'V'],
        [3, 'Brian Howell', 'VI'],
        [4, 'Lynne Foster', 'VI'],
        [5, 'Zachary Simon', 'VII']
    ]

    print({_[0]: _[1:] for _ in data})


if __name__ == "__main__":
    main()
