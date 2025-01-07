"""

Write a Python program to get the key, and value in a dictionary.

dict_num = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}

key  value
1     10
2     20
3     30
4     40
5     50
6     60

"""


def main():
    dict_num = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
    print("key\tvalue")
    for k, v in dict_num.items():
        print(f"{k}\t{v}")


if __name__ == "__main__":
    main()
