"""

Write a Python program that creates key-value list pairings within a dictionary.

{
    1: ['Jean Castro'], 2: ['Lula Powell'], 3: ['Brian Howell'], 4: ['Lynne Foster'], 5: ['Zachary Simon']
}

[{1: 'Jean Castro', 2: 'Lula Powell', 3: 'Brian Howell', 4: 'Lynne Foster', 5: 'Zachary Simon'}]

"""


def main():
    d = {
        1: ['Jean Castro'], 2: ['Lula Powell'], 3: ['Brian Howell'], 4: ['Lynne Foster'], 5: ['Zachary Simon']
    }

    print({k: v[0] for k, v in d.items()})


if __name__ == "__main__":
    main()
