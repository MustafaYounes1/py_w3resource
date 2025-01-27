"""

 Write a Python program to add two given lists using map and lambda.

[1, 2, 3]
[4, 5, 6]

[5, 7, 9]

"""


def main():
    lst1 = [1, 2, 3]
    lst2 = [4, 5, 6]
    print(list(map(sum, zip(lst1, lst2))))


if __name__ == "__main__":
    main()
