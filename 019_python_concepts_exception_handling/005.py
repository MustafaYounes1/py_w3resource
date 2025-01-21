"""

Write a Python program that opens a file and handles a PermissionError exception if there is a permission issue.

1. create the file that has the following contents: "Hello world"
2. make it read only
3. try to append a line at the end of it

"""

import platform
import subprocess


def main():
    try:
        # Create a file
        subprocess.call(["echo", "Hello world", ">", "005.txt"], shell=True)

        # make it read only
        if platform.system().lower() == "windows":
            subprocess.call(["attrib", "+r", "005.txt"], shell=True)

        else:
            raise SystemError("Expected a Windows machine")

        with open("005.txt", 'a') as f:
            f.write("Appended a line successfully\n")

    except PermissionError as e:
        print(e)

    except SystemError as e:
        print(e)


if __name__ == "__main__":
    main()
