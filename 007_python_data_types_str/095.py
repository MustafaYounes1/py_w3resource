"""

Write a Python program to convert the values of RGB components to a hexadecimal color code.

(255, 165, 1)       =>  FFA501
(255, 255, 255)     =>  FFFFFF
(0, 0, 0)           =>  000000
(255, 0, 0)         =>  FF0000
(0, 0, 128)         =>  000080
(192, 192, 192)     =>  C0C0C0

"""


def main():
    rgb = (0, 0, 128)
    print("".join([f"{_:02X}" for _ in rgb]))


if __name__ == "__main__":
    main()
