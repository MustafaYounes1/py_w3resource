"""

Write a Python program to listify the list of given strings individually using Python map.

['Red', 'Blue', 'Black', 'White', 'Pink']
[['R', 'e', 'd'], ['B', 'l', 'u', 'e'], ['B', 'l', 'a', 'c', 'k'], ['W', 'h', 'i', 't', 'e'], ['P', 'i', 'n', 'k']]

"""


def main():
    lst = ['Red', 'Blue', 'Black', 'White', 'Pink']
    print(list(map(list, lst)))


if __name__ == "__main__":
    main()
