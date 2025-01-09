"""

Write a Python program to invert a given dictionary with non-unique hashable values.

Convert the values to keys and keys to values as follows:

students = {
  'Ora Mckinney': 8,
  'Theodore Hollandl': 7,
  'Mae Fleming': 7,
  'Mathew Gilbert': 8,
  'Ivan Little': 7,
}

{8: ['Ora Mckinney', 'Mathew Gilbert'], 7: ['Theodore Hollandl', 'Mae Fleming', 'Ivan Little']}

"""

from collections import defaultdict


def main():
    students = {
        'Ora Mckinney': 8,
        'Theodore Hollandl': 7,
        'Mae Fleming': 7,
        'Mathew Gilbert': 8,
        'Ivan Little': 7,
    }

    out = defaultdict(list)
    for k, v in students.items():
        out[v].append(k)

    print(dict(out))


if __name__ == "__main__":
    main()
