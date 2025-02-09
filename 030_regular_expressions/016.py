"""

Write a Python program to remove leading zeros from an IP address.

216.08.094.196  =>  216.8.94.196

"""

import re


def main():
    ip = "216.08.094.196"
    print(re.sub(r"\b0*(\d+)", r"\1", ip))


if __name__ == "__main__":
    main()
