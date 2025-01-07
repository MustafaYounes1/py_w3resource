"""

Write a Python program to get the top three items in a shop.

{'item1': 45.50, 'item2': 35, 'item3': 41.30, 'item4':55, 'item5': 24}

item4 55
item1 45.5
item3 41.3

"""

from heapq import nlargest


def main():
    data = {'item1': 45.50, 'item2': 35, 'item3': 41.30, 'item4': 55, 'item5': 24}
    for k in nlargest(3, data, key=data.get):
        print(f"{k:6} {data[k]}")


if __name__ == "__main__":
    main()
