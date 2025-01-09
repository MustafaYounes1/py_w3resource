"""

Write a Python program to extract a list of values from a given list of dictionaries.

[{'Math': 90, 'Science': 92}, {'Math': 89, 'Science': 94}, {'Math': 92, 'Science': 88}]

Extract a list of values from said list of dictionaries where subject = Science
[92, 94, 88]


Extract a list of values from said list of dictionaries where subject = Math
[90, 89, 92]

"""


def main():
    d = [{'Math': 90, 'Science': 92}, {'Math': 89, 'Science': 94}, {'Math': 92, 'Science': 88}]
    print([_['Science'] for _ in d])
    print([_['Math'] for _ in d])


if __name__ == "__main__":
    main()
