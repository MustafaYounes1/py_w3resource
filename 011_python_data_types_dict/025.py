"""

Write a Python program to print a dictionary in table format.

my_dict = {'C1': [1, 2, 3], 'C2': [5, 6, 7], 'C3': [9, 10, 11]}

C1	C2	C3
1	5	9
2	6	10
3	7	11

"""


def main():
    my_dict = {'C1': [1, 2, 3], 'C2': [5, 6, 7], 'C3': [9, 10, 11]}
    print("\t".join(my_dict.keys()))
    for _ in zip(*my_dict.values()):
        print("\t".join(map(str, _)))


if __name__ == "__main__":
    main()
