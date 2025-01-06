"""

Write a Python program to find the XOR of two given strings interpreted as binary numbers.

Input:
['0001', '1011']
Output:
0b1010

Input:
['100011101100001', '100101100101110']
Output:
0b110001001111

"""

__data = [
    ['0001', '1011'],
    ['100011101100001', '100101100101110']
]


def main():
    for a, b in __data:
        print(
            bin(int(a, 2) ^ int(b, 2))
        )


if __name__ == "__main__":
    main()
