"""

Write a Python program to sum all the items in a dictionary.

my_dict = {'data1': 100, 'data2': -54, 'data3': 247}

=>  293

"""


def main():
    my_dict = {'data1': 100, 'data2': -54, 'data3': 247}
    print(sum(my_dict.values()))


if __name__ == "__main__":
    main()
