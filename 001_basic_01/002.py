"""

Write a Python program to find out what version of Python you are using.

"""

import platform
import sys


def main():
    # returns a string that contains the version number of the Python interpreter installed in the system.
    # It also returns additional information about the build number and the compiler used.
    print(f"sys: {sys.version}")

    # returns a tuple containing five components of the Python interpreter version number: the major version
    # release number, the minor version release number, the micro version release number, the release level,
    # and the serial number.
    print(f"sys: {sys.version_info}")

    # returns a string in the form major.minor.patch_level.
    print(f"platform: {platform.python_version()}")

    # returns a tuple in the form 'major', 'minor', 'patch_level'.
    print(f"platform: {platform.python_version_tuple()}")


if __name__ == "__main__":
    main()
