"""

Write a Python program to remove leading zeros from an IP address.

255.024.01.01   =>  255.24.1.1
127.0.0.01      =>  127.0.0.1

"""


def main():
    s = input("Enter the IP address: ")
    print(".".join([str(int(_)) for _ in s.split('.')]))


if __name__ == "__main__":
    main()
