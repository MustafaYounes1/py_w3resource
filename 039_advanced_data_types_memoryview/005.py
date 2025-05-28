"""

Write a Python function that takes two memory views and concatenates them. Print the concatenated memory view.

1st memory view on: b"Python"
2nd memory view on: b" Exercises!"
Out memory view on: b'Python Exercises!'

"""


def main():
    ba0, ba1 = b"Python", b" Exercises!"
    print(memoryview(ba0 + ba1).tobytes())


if __name__ == "__main__":
    main()
