"""

Write a Python program to get the height and width of the console window.

"""

# This module performs file control and I/O control on file descriptors. It is an interface to the
# fcntl() and ioctl() Unix routines.
# Important: Not available on Windows
import fcntl

# This module converts between Python values and C structs represented as Python bytes objects.
import struct

# This module provides an interface to the POSIX calls for tty I/O control.
import termios


def get_terminal_size():
    """
    This code queries the terminal's width (columns) and height (rows).
    It uses the 'TIOCGWINSZ' ioctl command to get window size information.

    uses the fcntl.ioctl() function to query the size of the terminal window using the termios.TIOCGWINSZ ioctl call.
    This call returns a struct.pack() object containing four integers representing the number of rows and columns of
    the terminal, as well as the horizontal and vertical pixel size.

    The struct.unpack() function is used to unpack the four integers from the struct.pack() object into separate
    variables th, tw, hp, and wp.

    :return: terminal size
    """

    # 1. Open file descriptor 0 (stdin, standard input stream).
    # 2. Call 'fcntl.ioctl' with 'TIOCGWINSZ' to fetch window size information into stdin.
    # 3. Unpack the received information into:
    #   'th' (height), 'tw' (width), 'hp' (horizontal pixel size), and 'wp' (vertical pixel size).

    th, tw, _, _ = struct.unpack(
        "HHHH",  # unsigned short
        fcntl.ioctl(
            0,
            termios.TIOCGWINSZ,
            struct.pack(
                "HHHH",
                0, 0, 0, 0
            )
        )
    )

    return th, tw


def main():
    print(f"Terminal size: {get_terminal_size()}")


if __name__ == "__main__":
    main()
