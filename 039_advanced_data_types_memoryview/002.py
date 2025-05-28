"""

Write a Python function that takes a memory view and converts it to a bytes object.

"""


def main():
    b = b"Python Exercises!"
    print(memoryview(b).tobytes())


if __name__ == "__main__":
    main()
