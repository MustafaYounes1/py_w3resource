"""

Write a Python program to convert a hexadecimal color code to a tuple of integers corresponding to its RGB components.

FFA501  =>  (255, 165, 1)
FFFFFF  =>  (255, 255, 255)
000000  =>  (0, 0, 0)
FF0000  =>  (255, 0, 0)
000080  =>  (0, 0, 128)
C0C0C0  =>  (192, 192, 192)

"""


def main():
    s = input("Enter the hexadecimal code: ")
    print(tuple(int(s[idx: idx + 2], 16) for idx in range(0, len(s), 2)))


if __name__ == "__main__":
    main()
