"""

Filter a list of dictionaries based on a key value.

lst = [{'name': 'Vivek', 'age': 25}, {'name': 'Esther', 'age': 22}, {'name': ' Neassa', 'age': 28}]
drop all people whose age is <= 23

"""


def main():
    lst = [{'name': 'Vivek', 'age': 25}, {'name': 'Esther', 'age': 22}, {'name': ' Neassa', 'age': 28}]
    print(list(filter(lambda d: d['age'] > 23, lst)))


if __name__ == "__main__":
    main()
