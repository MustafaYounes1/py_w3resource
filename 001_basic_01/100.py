"""

 Write a Python program to get the name of the host on which the routine is running.

"""

import socket


def main():
    print(f"Hostname: {socket.gethostname()}")


if __name__ == "__main__":
    main()
