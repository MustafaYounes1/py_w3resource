"""

Write a Python program that creates a memory view from a list of integers and print the hex values of each element.
    [8, 16, 42, 92, 128]    ->  08:10:2a:5c:80
"""


def main():
    mv = memoryview(bytes([8, 16, 42, 92, 128]))
    print(mv.hex(":"))


if __name__ == "__main__":
    main()
