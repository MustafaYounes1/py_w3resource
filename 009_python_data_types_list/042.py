"""

Write a Python program to find missing and additional values in two lists.

list1 = ['a', 'b', 'c', 'd', 'e', 'f']
list2 = ['d', 'e', 'f', 'g', 'h']

Missing values in second list: b,a,c
Additional values in second list: g,h

"""


def main():
    list1 = ['a', 'b', 'c', 'd', 'e', 'f']
    list2 = ['d', 'e', 'f', 'g', 'h']

    print(f"Missing values in second list: {','.join(set(list1) - set(list2))}")
    print(f"Additional values in second list: {','.join(set(list2) - set(list1))}")


if __name__ == "__main__":
    main()
