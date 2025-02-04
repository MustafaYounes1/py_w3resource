"""

Write a Python program to append text to a file and display the text.
    Input file: 003.txt
    Append the following line: 'Python Exercises'

Welcome to w3resource.com.
Append this text.Append this text.Append this text.
Append this text.
Append this text.
Append this text.
Append this text.
Python Exercises

"""

__in_file_path = "003.txt"


def main():
    with open(__in_file_path, 'a+') as f:
        f.write("Python Exercises\n")
        f.seek(0)
        contents = f.read()
        print(contents)


if __name__ == "__main__":
    main()
