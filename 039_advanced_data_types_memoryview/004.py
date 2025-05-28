"""

Write a Python program that reads a binary file into a memory view and saves a modified copy.

Note: Read the "004.bin" file and add 10 to each byte. (the expected modified binary data is: b'Hello world!')

"""

from pathlib import Path

# Hello world!
def main():
    input_file = Path("004.bin")
    assert input_file.is_file(), f"{input_file} doesn't exist"

    ba = bytearray(input_file.read_bytes())  # create a mutable bytes-like object

    mv = memoryview(ba)
    for idx in range(len(mv)):
        mv[idx] = (mv[idx] + 10) % 256  # Python only understands unsigned bytes in the range of 0-255

    out_file = Path("004_out.bin")
    out_file.write_bytes(mv)


if __name__ == "__main__":
    main()
