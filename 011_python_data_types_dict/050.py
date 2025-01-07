"""

A Python dictionary contains List as a value. Write a Python program to clear the list values in the said dictionary.

{'C1': [10, 20, 30], 'C2': [20, 30, 40], 'C3': [12, 34]}
{'C1': [], 'C2': [], 'C3': []}

"""


def main():
    data = {'C1': [10, 20, 30], 'C2': [20, 30, 40], 'C3': [12, 34]}

    for k in data:
        data[k].clear()

    print(data)


if __name__ == "__main__":
    main()
