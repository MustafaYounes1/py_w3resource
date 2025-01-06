"""

Write a Python program to get the system 'dir' command output.

"""

import subprocess


def main():
    # Run command with arguments and return its output.
    # 'universal_newlines=True' ensures text mode for cross-platform compatibility.
    output = subprocess.check_output("dir", shell=True, universal_newlines=True)
    print(output)


if __name__ == "__main__":
    main()
