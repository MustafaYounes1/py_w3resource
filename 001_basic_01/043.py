"""

Write a Python program to get OS name, platform and release information.

"""

import platform
import os


def main():
    # os name using os
    # The following names have currently been registered: 'posix', 'nt', 'java'.
    # provides the name of the operating system dependent module imported.
    print("Name of the operating system:", os.name)

    # os name using platform
    # returns the name of the operating system, such as 'Windows', 'Linux', or 'Darwin' (macOS).
    print("Name of the OS system:", platform.system())

    # os version using platform
    # returns the version or release of the operating system.
    print("Version of the operating system:", platform.release())


if __name__ == "__main__":
    main()
