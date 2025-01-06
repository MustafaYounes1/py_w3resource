"""

Write a Python program to remove key-value pairs from a list of dictionaries.

original_list = [{'key1': 'value1', 'key2': 'value2'}, {'key1': 'value3', 'key2': 'value4'}]

[{'key2': 'value2'}, {'key2': 'value4'}]

"""


def main():
    original_list = [{'key1': 'value1', 'key2': 'value2'}, {'key1': 'value3', 'key2': 'value4'}]

    for _ in original_list:
        _.pop("key1")

    print(original_list)


if __name__ == "__main__":
    main()
