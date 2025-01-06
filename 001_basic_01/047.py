"""

Write a Python program to find out the number of CPUs used.

"""

import multiprocessing
import os


def main():
    # using multiprocessing
    # supports spawning processes using an API similar to the threading module.
    # The multiprocessing package offers both local and remote concurrency, effectively side-stepping the Global
    # Interpreter Lock by using subprocesses instead of threads. Due to this, the multiprocessing module allows the
    # programmer to fully leverage multiple processors on a given machine.
    print(multiprocessing.cpu_count())

    # using os
    print(os.cpu_count())


if __name__ == "__main__":
    main()
