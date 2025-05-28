"""

Write a Python program that creates a memory view on a bytes object and prints the length and first 8 bytes.

b"Python Exercises!"

#bytes: 17
first 8 bytes: b'Python E'

"""


def main():
    b = b"Python Exercises!"

    mv = memoryview(b)
    print(f"#bytes: {mv.nbytes}")
    print(f"first 8 bytes: {mv[:8].tobytes()}")


if __name__ == "__main__":
    main()
