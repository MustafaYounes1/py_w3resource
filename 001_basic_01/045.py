"""

Write a Python program that calls an external command.

e.g. "python -V"

"""

import os
from subprocess import call


def main():
    # using subprocess
    # allows us to spawn new processes, connect to their input/output/error pipes, and obtain their return codes.
    call(["python", "-V"])

    # using os
    # provides a portable way of using operating system dependent functionality.
    os.system("python -V")


if __name__ == "__main__":
    main()
