"""

Write a Python program to write a list to a file.
    Output file: 011.txt
    data: ["w3resource.com", "Python", "File IO", "Exercise 11"]

011.txt should get created and would have the following content:

w3resource.com
Python
File IO
Exercise 11

"""

__out_file_path = "011.txt"


def main():
    lines = ["w3resource.com", "Python", "File IO", "Exercise 11"]

    with open(__out_file_path, "w") as f:
        for line in lines:
            f.write(line + "\n")


if __name__ == "__main__":
    main()
