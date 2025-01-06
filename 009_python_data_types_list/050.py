"""

Write a Python program to sort a list of nested dictionaries as follows.

my_list = [{'key': {'subkey': 1}}, {'key': {'subkey': 10}}, {'key': {'subkey': 5}}]

[{'key': {'subkey': 10}}, {'key': {'subkey': 5}}, {'key': {'subkey': 1}}]

"""


def main():
    my_list = [{'key': {'subkey': 1}}, {'key': {'subkey': 10}}, {'key': {'subkey': 5}}]
    print(sorted(my_list, key=lambda d: d['key']['subkey'], reverse=True))


if __name__ == "__main__":
    main()
