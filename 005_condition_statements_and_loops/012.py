"""

Write a Python program that accepts a sequence of lines (blank line to terminate) as input and prints the lines as
output (all characters in lower case)

"""


def main():
    lines = []

    while True:
        line = input("Enter a line or a blank line to terminate: ")
        if not line:
            break
        lines.append(line.lower())

    print("\n".join(lines))


if __name__ == "__main__":
    main()
